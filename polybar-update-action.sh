#!/usr/bin/env bash

gnome-terminal -e 'sh -c "echo Synchronizing Packages; echo ----------------------;sudo apt update; echo ;echo Starting Package Upgrade; echo ------------------------; sudo apt upgrade; echo ;echo Refreshing Cache; echo ----------------; check-updates.py; echo ; echo System update finished.; echo -----------------------; exec zsh"'
