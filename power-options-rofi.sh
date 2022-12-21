#!/usr/bin/env bash

CHOICE=$( echo -en "Suspend\0icon\x1fpreferences-desktop-screensaver\nReboot\0icon\x1fsystem-reboot\nPoweroff\0icon\x1fsystem-shutdown\nWindows\0icon\x1f/home/mukul/.icons/Windows_logo_-_2021.svg\nLogout\0icon\x1fsystem-log-out\n" | rofi -dmenu -i -p "⏻     Please select an option:" )

if [ x"Suspend" = x"${CHOICE}" ]
then
    confirm-suspend.sh
elif [ x"Reboot" = x"${CHOICE}" ]
then
    confirm-reboot.sh
elif [ x"Poweroff" = x"${CHOICE}" ]
then
    confirm-poweroff.sh
elif [ x"Windows" = x"${CHOICE}" ]
then
    confirm-reboot-windows.sh
elif [ x"Logout" = x"${CHOICE}" ]
then
    confirm-logoff.sh
else
    exit 0
fi