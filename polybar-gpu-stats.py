#!/usr/bin/env python3

import subprocess
import sys

GPU_TEMP_COMMAND = (
    "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits"
)
GPU_USAGE_COMMAND = (
    "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits"
)

mode = ""
if len(sys.argv) >= 2:
    mode = sys.argv[1]

command_output = ""
output = ""

if mode == "USAGE":
    command_output = subprocess.run(
        GPU_USAGE_COMMAND.split(" "), capture_output=True
    ).stdout.decode("UTF-8")
elif mode == "TEMP":
    command_output = subprocess.run(
        GPU_TEMP_COMMAND.split(" "), capture_output=True
    ).stdout.decode("UTF-8")

if command_output:
    output = command_output.replace("\n", "")
print(output)
