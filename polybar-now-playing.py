#!/usr/bin/python3 -u

import gi
import json

gi.require_version("Playerctl", "2.0")
from gi.repository import GLib, Playerctl

ICON_TITLE = ""
ICON_PLAY = ""
ICON_PAUSE = ""
ICON_NEXT = ""
ICON_PREVIOUS = ""

MAX_LENGTH_TITLE = 40
MAX_LENGTH_ARTIST = 25

manager = Playerctl.PlayerManager()


def print_weather_output():
    with open("/home/mukul/.cache/weather.json", "rt") as f:
        data = json.load(f)
        weather_icon = " "
        w_condition = data["weather"][0]["main"]
        w_city = data["name"]
        w_country = data["sys"]["country"]
        w_temp = str(int(round(float(data["main"]["temp"])))) + "°C"
        if w_condition == "Clear":
            weather_icon = " "
        elif w_condition == "Clouds":
            weather_icon = " "
        elif w_condition == "Drizzle":
            weather_icon = " "
        elif w_condition == "Rain":
            weather_icon = " "
        elif w_condition == "Thunderstorm":
            weather_icon = " "
        elif w_condition == "Snow":
            weather_icon = " "
        elif w_condition in [
            "Mist",
            "Smoke",
            "Haze",
            "Dust",
            "Fog",
            "Sand",
            "Dust",
            "Ash",
            "Squall",
            "Tornado",
        ]:
            weather_icon = " "
        print(
            "%{T3}"
            + weather_icon
            + "%{T-}  "
            + w_temp
            + "  "
            + w_condition
            + " in "
            + w_city
            + ", "
            + w_country
        )


def print_music_output(player):
    artist = player.get_artist()
    title = player.get_title()
    if artist and title:
        if len(artist) > MAX_LENGTH_ARTIST:
            artist = artist[:MAX_LENGTH_ARTIST] + "..."
        if len(title) > MAX_LENGTH_TITLE:
            title = title[:MAX_LENGTH_TITLE] + "..."
        if player.props.status == "Playing":
            print(
                "%{T3}"
                + ICON_TITLE
                + "%{T-}  "
                + artist
                + " - "
                + title
                + "  %{T3}%{A1:playerctl previous:}"
                + ICON_PREVIOUS
                + "%{A}  %{A1:playerctl play-pause:}"
                + ICON_PAUSE
                + "%{A}  %{A1:playerctl next:}"
                + ICON_NEXT
                + "%{A}%{T-}"
            )
        else:
            print(
                "%{T3}"
                + ICON_TITLE
                + "%{T-}  "
                + artist
                + " - "
                + title
                + "  %{T3}%{A1:playerctl previous:}"
                + ICON_PREVIOUS
                + "%{A}  %{A1:playerctl play-pause:}"
                + ICON_PLAY
                + "%{A}  %{A1:playerctl next:}"
                + ICON_NEXT
                + "%{A}%{T-}"
            )
    else:
        print_weather_output()


def on_play(player, status, manager):
    print_music_output(player)


def on_pause(player, status, manager):
    print_music_output(player)


def on_metadata(player, metadata, manager):
    print_music_output(player)


def on_name_appeared(manager, name):
    init_player(name)


def init_player(name):
    player = Playerctl.Player.new_from_name(name)
    player.connect("playback-status::playing", on_play, manager)
    player.connect("playback-status::paused", on_pause, manager)
    player.connect("metadata", on_metadata, manager)
    manager.manage_player(player)
    print_music_output(player)


manager.connect("name-appeared", on_name_appeared)

for name in manager.props.player_names:
    init_player(name)

# wait for events
main = GLib.MainLoop()
main.run()
