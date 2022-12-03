#!/usr/bin/env bash

warp_status=$(ifconfig CloudflareWARP 2>&1)

if [[ $warp_status == *"Device not found"* ]]; then
    echo ""
else
    echo 
fi
