#!/usr/bin/env python3

import re

with open("/home/mukul/.config/polybar/config", "rt") as f:
    data = f.read()

if re.search(r"(modules-right\s\=\s.*)date(\s)", data):
    result = re.sub(r"(modules-right\s\=\s.*)date(\s)", r"\1date-details\2", data)

if re.search(r"(modules-right\s\=\s.*)date-details(\s)", data):
    result = re.sub(r"(modules-right\s\=\s.*)date-details(\s)", r"\1date\2", data)

with open("/home/mukul/.config/polybar/config", "wt") as f:
    f.write(result)
