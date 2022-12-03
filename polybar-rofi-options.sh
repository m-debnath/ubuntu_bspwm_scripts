#!/usr/bin/env bash

CHOICE=$( echo -en "Toggle System Stats\0icon\x1futilities-system-monitor\nToggle System Tray\0icon\x1fapplications-system\nToggle Seconds in Panel\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/time.svg\nReload Panel\0icon\x1fsystem-reboot\n" | rofi -dmenu -i -p "    Please select one of the options for Polybar:" )

if [ x"Toggle Seconds in Panel" = x"${CHOICE}" ]
then
    polybar-toggle-date-format.py
elif [ x"Toggle System Tray" = x"${CHOICE}" ]
then
    polybar-toggle-tray.sh
elif [ x"Toggle System Stats" = x"${CHOICE}" ]
then
    polybar-toggle-system-stats.py
elif [ x"Reload Panel" = x"${CHOICE}" ]
then
    polybar-msg cmd restart
else
    exit 0
fi