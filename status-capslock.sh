#!/usr/bin/env bash

ICON_CAPSLOCK_ON="capslock-on"
ICON_CAPSLOCK_OFF="capslock-off"
ICON=$ICON_NUMLOCK_OFF

APP_NAME="Caps_Lock Status"
APP_ID="12677"

CAPS_STATUS=$(xset -q | sed -n 's/^.*Caps Lock:\s*\(\S*\).*$/\1/p')

if [[ "$CAPS_STATUS" = "on" ]]
then
  ICON=$ICON_CAPSLOCK_ON
else
  ICON=$ICON_CAPSLOCK_OFF
fi

dunstify -r "$APP_ID" -a "$APP_NAME" -i "$ICON" "Capslock is $CAPS_STATUS"