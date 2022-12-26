#!/usr/bin/env bash

ICON_NUMLOCK_ON="numlock-on"
ICON_NUMLOCK_OFF="numlock-off"
ICON=$ICON_NUMLOCK_OFF

APP_NAME="Num_Lock Status"
APP_ID="12678"

NUM_STATUS=$(xset -q | sed -n 's/^.*Num Lock:\s*\(\S*\).*$/\1/p')

if [[ "$NUM_STATUS" = "on" ]]
then
  ICON=$ICON_NUMLOCK_ON
else
  ICON=$ICON_NUMLOCK_OFF
fi

dunstify -r "$APP_ID" -a "$APP_NAME" -i "$ICON" "Numlock is $NUM_STATUS"