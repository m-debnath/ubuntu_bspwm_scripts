#!/usr/bin/env bash

warp_status=$(pacmd list-sources | grep RUNNING 2>&1)

if [[ $warp_status == *"RUNNING"* ]]; then
    echo ""
else
    echo ""
fi
