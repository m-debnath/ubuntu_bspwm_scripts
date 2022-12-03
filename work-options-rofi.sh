#!/usr/bin/env bash

CHOICE=$( echo -en "One Cognizant\0icon\x1f/home/mukul/.icons/onecognizant.png\nCognizant Teams\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/categories/teams.svg\nCognizant Webmail\0icon\x1f/usr/share/icons/Papirus-Dark/symbolic/status/mail-unread-symbolic.svg\nCognizant Timesheet\0icon\x1f/usr/share/icons/Papirus-Dark/16x16/panel/dino-status-away.svg\nCognizant Trutime\0icon\x1f/home/mukul/.icons/fingerprint_icon.png\nTele2 Webmail\0icon\x1f/home/mukul/.icons/T2.png\n" | rofi -dmenu -i -p "💼   Let's get some work done:" )

if [ x"One Cognizant" = x"${CHOICE}" ]
then
    google-chrome --new-window https://onecognizant.cognizant.com/
elif [ x"Cognizant Teams" = x"${CHOICE}" ]
then
    google-chrome --new-window https://teams.microsoft.com/
elif [ x"Cognizant Webmail" = x"${CHOICE}" ]
then
    google-chrome --new-window https://outlook.office365.com/mail/
elif [ x"Cognizant Timesheet" = x"${CHOICE}" ]
then
    google-chrome --new-window https://compass.esa.cognizant.com/psc/ESA89PRD/EMPLOYEE/ERP/c/ADMINISTER_EXPENSE_FUNCTIONS.CTS_TS_LAND_COMP.GBL
elif [ x"Cognizant Trutime" = x"${CHOICE}" ]
then
    google-chrome --new-window https://onecognizantbcazrapps.cognizant.com/2185/#
elif [ x"Tele2 Webmail" = x"${CHOICE}" ]
then
    google-chrome -incognito --new-window https://outlook.office365.com/mail/
else
    exit 0
fi