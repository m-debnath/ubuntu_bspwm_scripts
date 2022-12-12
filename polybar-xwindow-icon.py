#!/usr/bin/python3 -u
"""python-xlib example which reacts to changing the active window/title.

Requires:
- Python
- python-xlib

Tested with Python 2.x because my Kubuntu 14.04 doesn't come with python-xlib
for Python 3.x.

Design:
-------

Any modern window manager that isn't horrendously broken maintains an X11
property on the root window named _NET_ACTIVE_WINDOW.

Any modern application toolkit presents the window title via a property
named _NET_WM_NAME.

This listens for changes to both of them and then hides duplicate events
so it only reacts to title changes once.

Known Bugs:
-----------

- Under some circumstances, I observed that the first window creation and last
  window deletion on on an empty desktop (ie. not even a taskbar/panel) would
  go ignored when using this test setup:

      Xephyr :3 &
      DISPLAY=:3 openbox &
      DISPLAY=:3 python3 x11_watch_active_window.py

      # ...and then launch one or more of these in other terminals
      DISPLAY=:3 leafpad
"""

import sys
from contextlib import contextmanager
from typing import Any, Dict, Optional, Tuple, Union  # noqa

from Xlib import X
from Xlib.display import Display
from Xlib.error import XError
from Xlib.protocol.rq import Event
from Xlib.xobject.drawable import Window

mode = ""
if len(sys.argv) >= 2:
    mode = sys.argv[1]

# Connect to the X server and get the root window
disp = Display()
root = disp.screen().root

# Prepare the property names we use so they can be fed into X11 APIs
NET_ACTIVE_WINDOW = disp.intern_atom("_NET_ACTIVE_WINDOW")
NET_WM_NAME = disp.intern_atom("_NET_WM_NAME")  # UTF-8
WM_NAME = disp.intern_atom("WM_NAME")  # Legacy encoding
WM_CLASS = disp.intern_atom("WM_CLASS")

DEFAULT_ICON_FONT = "5"  # Linked to polybar config
DEFAULT_ICON = ""
DEFAULT_ICON_COLOR = "#ffffff"
DEFAULT_TITLE_LENGTH = 60
DEFAULT_ICON_SPACING = 2

last_seen = {"xid": None, "title": None, "class": None}  # type: Dict[str, Any]


@contextmanager
def window_obj(win_id: Optional[int]) -> Window:
    window_obj = None
    if win_id:
        try:
            window_obj = disp.create_resource_object("window", win_id)
        except XError:
            pass
    yield window_obj


def get_active_window() -> Tuple[Optional[int], bool]:
    try:
        response = root.get_full_property(NET_ACTIVE_WINDOW, X.AnyPropertyType)
        if not response:
            return None, False
        win_id = response.value[0]

        focus_changed = win_id != last_seen["xid"]
        if focus_changed:
            with window_obj(last_seen["xid"]) as old_win:
                if old_win:
                    old_win.change_attributes(event_mask=X.NoEventMask)

            last_seen["xid"] = win_id
            with window_obj(win_id) as new_win:
                if new_win:
                    new_win.change_attributes(event_mask=X.PropertyChangeMask)

        return win_id, focus_changed
    except Exception:
        return None, False


def _get_window_name_inner(win_obj: Window) -> str:
    for atom in (NET_WM_NAME, WM_NAME):
        try:
            window_name = win_obj.get_full_property(atom, 0)
        except UnicodeDecodeError:  # Apparently a Debian distro package bug
            title = "<could not decode characters>"
        except Exception:
            title = "<could not decode characters>"
        else:
            if window_name:
                win_name = window_name.value  # type: Union[str, bytes]
                if isinstance(win_name, bytes):
                    # Apparently COMPOUND_TEXT is so arcane that this is how
                    # tools like xprop deal with receiving it these days
                    win_name = win_name.decode("utf-8", "replace")
                return win_name
            else:
                title = "<unnamed window>"

    return "{} (XID: {})".format(title, win_obj.id)


def _get_window_class_inner(win_obj: Window) -> str:
    try:
        window_class = win_obj.get_full_property(WM_CLASS, 0)
        return "{}".format(window_class.value.decode("UTF-8").split("\x00")[1])
    except Exception:
        return ""


def get_window_name(win_id: Optional[int]) -> Tuple[Optional[str], bool]:
    if not win_id:
        last_seen["title"] = None
        return last_seen["title"], True

    title_changed = False
    with window_obj(win_id) as wobj:
        if wobj:
            try:
                win_title = _get_window_name_inner(wobj)
                win_class = _get_window_class_inner(wobj)
            except XError:
                pass
            except Exception:
                pass
            else:
                title_changed = win_title != last_seen["title"]
                last_seen["title"] = win_title
                last_seen["class"] = win_class

    return last_seen["title"], title_changed


def handle_xevent(event: Event):
    if event.type != X.PropertyNotify:
        return

    changed = False
    if event.atom == NET_ACTIVE_WINDOW:
        if get_active_window()[1]:
            get_window_name(last_seen["xid"])  # Rely on the side-effects
            changed = True
    elif event.atom in (NET_WM_NAME, WM_NAME):
        changed = changed or get_window_name(last_seen["xid"])[1]

    if changed:
        handle_change(last_seen)


def handle_change(new_state: dict):
    if mode == "DEBUG":
        print(new_state)
        return
    if not new_state["title"]:
        print("")
        return
    output_icon_font = DEFAULT_ICON_FONT
    output_icon = DEFAULT_ICON
    output_icon_color = DEFAULT_ICON_COLOR
    output_icon_spacing = DEFAULT_ICON_SPACING
    output_title = new_state["title"]
    if len(output_title) > DEFAULT_TITLE_LENGTH:
        output_title = output_title[: DEFAULT_TITLE_LENGTH - 3] + "..."
    if new_state["class"] == "Gnome-terminal":
        output_icon = ""
        output_icon_font = "6"
        output_icon_spacing = 1
    elif new_state["class"] == "Gnome-system-monitor":
        output_icon = ""
    elif new_state["class"] == "Code":
        output_icon = ""
        output_icon_font = "6"
        output_icon_color = "#0074C2"
        output_icon_spacing = 1
    elif (
        new_state["class"] == "Gedit"
        or new_state["class"] == "Notepadqq"
        or new_state["class"] == "libreoffice-writer"
    ):
        output_icon = ""
    elif new_state["class"] == "Org.gnome.Nautilus":
        output_icon = ""
    elif new_state["class"] == "Gnome-calculator":
        output_icon = ""
    elif new_state["class"] == "Font-manager" or new_state["class"] == "Gucharmap":
        output_icon = ""
    elif (
        new_state["class"] == "Gimp-2.10"
        or new_state["class"] == "Eog"
        or new_state["class"] == "Shotwell"
    ):
        output_icon = ""
    elif new_state["class"] == "MyPaint" or new_state["class"] == "libreoffice-draw":
        output_icon = ""
        output_icon_font = "7"
    elif new_state["class"] == "flameshot":
        output_icon = ""
    elif new_state["class"] == "Totem" or new_state["class"] == "vlc":
        output_icon = ""
    elif new_state["class"] == "Pavucontrol" or new_state["class"] == "Rhythmbox":
        output_icon = ""
    elif (
        new_state["class"] == "Gnome-control-center"
        or new_state["class"] == "Gnome-tweaks"
        or new_state["class"] == "Nvidia-settings"
    ):
        output_icon = ""
    elif (
        new_state["class"] == "Update-manager"
        or new_state["class"] == "Software-properties-gtk"
    ):
        output_icon = ""
    elif new_state["class"] == "Gnome-mines":
        output_icon = ""
    elif new_state["class"] == "Evince":
        output_icon = ""
    elif new_state["class"] == "Google-chrome" or new_state["class"] == "firefox":
        chrome_icon = ""
        firefox_icon = ""
        if new_state["title"].startswith("Gmail") or "- Gmail" in new_state["title"]:
            output_icon = ""
        elif (
            new_state["title"].startswith("Facebook")
            or "- Facebook" in new_state["title"]
        ):
            output_icon = ""
            output_icon_color = "#2374E1"
        elif (
            new_state["title"].startswith("Twitter")
            or "/ Twitter" in new_state["title"]
        ):
            output_icon = ""
            output_icon_color = "#1C98EB"
        elif (
            new_state["title"].startswith("YouTube")
            or "- YouTube" in new_state["title"]
        ):
            output_icon = ""
            output_icon_color = "#FF0000"
        elif (
            new_state["title"].startswith("Amazon.in")
            or "- Amazon.in" in new_state["title"]
        ):
            output_icon = ""
        elif (
            new_state["title"].startswith("Google Maps")
            or "- Google Maps" in new_state["title"]
        ):
            output_icon = ""
        elif (
            new_state["title"].startswith("iCloud") or "- iCloud" in new_state["title"]
        ):
            output_icon = ""
        elif new_state["title"].startswith("Apple TV+"):
            output_icon = ""
        elif (
            new_state["title"].startswith("LinkedIn")
            or "| LinkedIn" in new_state["title"]
        ):
            output_icon = ""
            output_icon_color = "#0073B2"
        elif new_state["title"].startswith("WhatsApp"):
            output_icon = ""
            output_icon_color = "#0DC143"
        elif (
            new_state["title"].startswith("Stack Overflow")
            or "- Stack Overflow" in new_state["title"]
        ):
            output_icon = ""
            output_icon_color = "#F2740D"
        else:
            if new_state["class"] == "Google-chrome":
                output_icon = chrome_icon
            elif new_state["class"] == "firefox":
                output_icon = firefox_icon
    print(
        "%{T"
        + output_icon_font
        + "}%{F"
        + output_icon_color
        + "}"
        + output_icon
        + "%{F-}%{T-}"
        + (" " * output_icon_spacing)
        + output_title
    )


if __name__ == "__main__":
    # Listen for _NET_ACTIVE_WINDOW changes
    root.change_attributes(event_mask=X.PropertyChangeMask)

    # Prime last_seen with whatever window was active when we started this
    get_window_name(get_active_window()[0])
    handle_change(last_seen)

    while True:  # next_event() sleeps until we get an event
        handle_xevent(disp.next_event())
