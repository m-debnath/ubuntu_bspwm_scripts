#!/usr/bin/env python3

with open("/home/mukul/.config/polybar/config", "rt") as f:
    data = f.read()


if (
    "xkeyboard sep sep cpu gpu-usage memory filesystem homefilesystem check_update"
    in data
):
    result = data.replace(
        "xkeyboard sep sep cpu gpu-usage memory filesystem homefilesystem check_update",
        "xkeyboard sep sep check_update",
    )
elif "xkeyboard sep sep check_update" in data:
    result = data.replace(
        "xkeyboard sep sep check_update",
        "xkeyboard sep sep cpu gpu-usage memory filesystem homefilesystem check_update",
    )
else:
    result = data

with open("/home/mukul/.config/polybar/config", "wt") as f:
    f.write(result)
