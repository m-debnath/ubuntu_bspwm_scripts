#!/usr/bin/env python3

import re
import subprocess

UPDATE_CHECK_COMMAND = "sudo apt update"

UPDATES_NOT_AVAILABLE = "All packages are up to date"
UPDATES_AVAILABLE = "(\d+)\s*packages? can be upgraded"
UPDATES_AVAILABLE_PATTERN = re.compile(UPDATES_AVAILABLE, flags=re.MULTILINE)

output = str(subprocess.run(UPDATE_CHECK_COMMAND.split(" "), capture_output=True))
update_count = "0"

if not UPDATES_NOT_AVAILABLE in output:
    result = re.search(UPDATES_AVAILABLE_PATTERN, output)
    if result and len(result.groups()) > 0:
        update_count = result.groups()[0]

# print(update_count)

with open("/home/mukul/.cache/available_updates.json", "wt") as f:
    f.write(update_count)
