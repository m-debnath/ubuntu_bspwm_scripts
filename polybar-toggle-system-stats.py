#!/usr/bin/env python3

with open("/home/mukul/.config/polybar/config", "rt") as f:
    data = f.read()


if (
    "xkeyboard sep sep sep-primary cpu gpu-usage memory filesystem homefilesystem check_update"
    in data
):
    result = data.replace(
        "xkeyboard sep sep sep-primary cpu gpu-usage memory filesystem homefilesystem check_update",
        "xkeyboard sep sep sep-primary check_update",
    )
elif "xkeyboard sep sep sep-primary check_update" in data:
    result = data.replace(
        "xkeyboard sep sep sep-primary check_update",
        "xkeyboard sep sep sep-primary cpu gpu-usage memory filesystem homefilesystem check_update",
    )
else:
    result = data

with open("/home/mukul/.config/polybar/config", "wt") as f:
    f.write(result)
