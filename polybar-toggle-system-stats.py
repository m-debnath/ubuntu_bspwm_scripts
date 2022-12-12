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


# if "cpu gpu-usage memory" in data and "memory filesystem homefilesystem check_update" in data:
#     result = data.replace("cpu gpu-usage memory", "cpu memory").replace(
#         "memory filesystem homefilesystem check_update", "memory check_update"
#     )
# elif "cpu memory" in data and "memory check_update" in data:
#     result = data.replace("cpu memory", "cpu gpu-usage memory").replace(
#         "memory check_update", "memory filesystem homefilesystem check_update"
#     )

with open("/home/mukul/.config/polybar/config", "wt") as f:
    f.write(result)
