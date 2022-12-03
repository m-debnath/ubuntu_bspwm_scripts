#!/usr/bin/env python3

import re
import subprocess
import sys

MAX_VOLUME = 100
MIN_VOLUME = 0
VOLUME_STEP = 2

GET_VOLUME_COMMAND = "pactl get-sink-volume @DEFAULT_SINK@"
INCREASE_VOLUME_COMMAND = f"pactl set-sink-volume @DEFAULT_SINK@ +{VOLUME_STEP}%"
DECREASE_VOLUME_COMMAND = f"pactl set-sink-volume @DEFAULT_SINK@ -{VOLUME_STEP}%"
INCREASE_NOTIFICATION_COMMAND = (
    'dunstify -a "changeVolume" -u low -i audio-volume-high -r "597413" "Volume: VOL_LEVEL%"'
)
DECREASE_NOTIFICATION_COMMAND = (
    'dunstify -a "changeVolume" -u low -i audio-volume-medium -r "597413" "Volume: VOL_LEVEL%"'
)

VOLUME_REGEX = "front-left:.*?\/\s+(\d+%)"
VOLUME_REGEX_PATTERN = re.compile(VOLUME_REGEX, flags=re.MULTILINE)

mode = ""
if len(sys.argv) >= 2:
    mode = sys.argv[1]

volume_command_output = str(subprocess.run(GET_VOLUME_COMMAND.split(" "), capture_output=True))

volume = 0
result = re.search(VOLUME_REGEX_PATTERN, volume_command_output)
if result and len(result.groups()) > 0:
    volume = int(result.groups()[0][:-1])

if mode == "INCREASE" and not volume + VOLUME_STEP > MAX_VOLUME:
    subprocess.run(INCREASE_VOLUME_COMMAND.split(" "))
    subprocess.run(
        INCREASE_NOTIFICATION_COMMAND.replace("VOL_LEVEL", str(volume + VOLUME_STEP)), shell=True
    )

if mode == "DECREASE" and not volume - VOLUME_STEP < MIN_VOLUME:
    subprocess.run(DECREASE_VOLUME_COMMAND.split(" "))
    subprocess.run(
        DECREASE_NOTIFICATION_COMMAND.replace("VOL_LEVEL", str(volume - VOLUME_STEP)), shell=True
    )
