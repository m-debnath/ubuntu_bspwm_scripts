#!/usr/bin/env bash

CHOICE=$( echo -en "Yes\0icon\x1fobject-select-symbolic\nNo\0icon\x1fwindow-close-symbolic\n"  | rofi -dmenu -i -p "    Do you really want to logoff?" )

if [ x"Yes" = x"${CHOICE}" ]
then
    # i3-msg exit
    bspc quit
    # pkill -KILL -u mukul
else
    exit 0
fi