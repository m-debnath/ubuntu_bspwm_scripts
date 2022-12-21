#!/usr/bin/env bash

CHOICE=$( echo -en "Yes\0icon\x1fobject-select-symbolic\nNo\0icon\x1fwindow-close-symbolic\n" | rofi -dmenu -i -p "😴   Do you really want to suspend?" )

if [ x"Yes" = x"${CHOICE}" ]
then
    systemctl suspend
else
    exit 0
fi