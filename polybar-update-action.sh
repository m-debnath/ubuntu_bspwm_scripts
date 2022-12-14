#!/usr/bin/env bash

gnome-terminal -e 'sh -c "echo Synchronizing Packages; echo ----------------------;sudo apt update; echo ;echo Starting Software Update; echo ------------------------; sudo apt upgrade; echo ;echo Refreshing Cache; echo ----------------; check-updates.py; echo ; echo Software Update finished.; echo -------------------------; exec zsh"'
