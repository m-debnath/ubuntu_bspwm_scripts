#!/usr/bin/env bash

CHOICE=$( echo -en "Yes\0icon\x1fobject-select-symbolic\nNo\0icon\x1fwindow-close-symbolic\n" | rofi -dmenu -i -p "     Do you really want to reboot to Windows 11?" )

if [ x"Yes" = x"${CHOICE}" ]
then
    reboot-to-windows.sh
else
    exit 0
fi