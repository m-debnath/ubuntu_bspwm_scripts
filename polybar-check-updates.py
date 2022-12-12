#!/usr/bin/env python3

update_count = "0"

try:
    with open("/home/mukul/.cache/available_updates.json", "rt") as f:
        update_count = f.readline()
except OSError:
    pass

if update_count == "0":
    print("")
else:
    print(update_count)
