#!/usr/bin/env bash

if grep -Fxq "tray-position = none" /home/mukul/.config/polybar/config
then
    sed -i 's/tray-position = none/tray-position = right/g' /home/mukul/.config/polybar/config
    sed -i 's/ powermenu/ powermenu sep sep/g' /home/mukul/.config/polybar/config
    exit 0
fi

if grep -Fxq "tray-position = right" /home/mukul/.config/polybar/config
then
    sed -i 's/tray-position = right/tray-position = none/g' /home/mukul/.config/polybar/config
    sed -i 's/ powermenu sep sep/ powermenu/g' /home/mukul/.config/polybar/config
    exit 0
fi
