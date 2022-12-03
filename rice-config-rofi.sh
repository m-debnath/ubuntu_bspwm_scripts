#!/usr/bin/env bash

CHOICE=$( echo -en "My Scripts\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/bash.svg\nWindow Manager (bspwm)\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/window_list.svg\nKeybindings (sxhkd)\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/key_bindings.svg\nTop Panel (polybar)\0icon\x1f/usr/share/icons/Papirus-Dark/48x48/categories/org.kde.windowappmenu.svg\nDesktop Widgets (conky)\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/conky.svg\nApplication Launcher (rofi)\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/pop-cosmic-launcher.svg\nNotification Daemon (dunst)\0icon\x1f/usr/share/icons/Papirus-Dark/symbolic/status/notification-symbolic.svg\nMenu System (jgmenu)\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/menulibre.svg\nWindow Compositor (picom)\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/picom.svg\n" | rofi -dmenu -i -p "    Please select to edit config:" )

if [ x"My Scripts" = x"${CHOICE}" ]
then
    code ~/scripts/
elif [ x"Window Manager (bspwm)" = x"${CHOICE}" ]
then
    code ~/.config/bspwm/
elif [ x"Keybindings (sxhkd)" = x"${CHOICE}" ]
then
    code ~/.config/sxhkd/
elif [ x"Top Panel (polybar)" = x"${CHOICE}" ]
then
    code ~/.config/polybar/
elif [ x"Desktop Widgets (conky)" = x"${CHOICE}" ]
then
    code ~/.config/conky/
elif [ x"Application Launcher (rofi)" = x"${CHOICE}" ]
then
    code ~/.config/rofi/
elif [ x"Notification Daemon (dunst)" = x"${CHOICE}" ]
then
    code ~/.config/dunst/
elif [ x"Menu System (jgmenu)" = x"${CHOICE}" ]
then
    code ~/.config/jgmenu/
elif [ x"Window Compositor (picom)" = x"${CHOICE}" ]
then
    code ~/.config/picom/
else
    exit 0
fi