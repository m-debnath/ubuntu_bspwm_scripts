#!/usr/bin/env bash

output=""

battery_level=$(upower -i /org/freedesktop/UPower/devices/mouse_hidpp_battery_1 | grep -E "percentage" | awk '{ print substr($2, 1, length($2)-1) }')

if [[ battery_level -lt 20 ]]
then
    output=""
fi

echo "$output"