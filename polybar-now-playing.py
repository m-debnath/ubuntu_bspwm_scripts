#!/usr/bin/python3 -u

import json
import subprocess
from time import sleep

excluded_list = [
    "Prime Video",
    "Netflix",
    "Disney+ Hotstar",
    "FMovies",
    "Facebook",
    "Twitter",
    "Microsoft Teams",
    "XVideos.com",
    "JioCinema",
]

SLEEP_INTERVAL = 0.25

ICON_TITLE = ""
ICON_PLAY = ""
ICON_PAUSE = ""
ICON_NEXT = ""
ICON_PREVIOUS = ""

music_title = ""
music_artist = ""
output = ""

TITLE_COMMAND = "playerctl metadata -f {{title}}"
ARTIST_COMMAND = "playerctl metadata -f {{trunc(artist,25)}}"
STATUS_COMMAND = "playerctl status"

STATUS_PLAY = "Playing"
STATUS_PAUSE = "Paused"

def print_weather():
    with open("/home/mukul/.cache/weather.json", "rt") as f:
        data = json.load(f)
        weather_icon = " "
        w_condition = data["weather"][0]["main"]
        w_city = data["name"]
        w_country = data["sys"]["country"]
        w_temp = str(int(round(float(data["main"]["temp"])))) + "°C"
        if w_condition == "Clear":
            weather_icon = " "
        elif w_condition == "Clouds":
            weather_icon = " "
        elif w_condition == "Drizzle":
            weather_icon = " "
        elif w_condition == "Rain":
            weather_icon = " "
        elif w_condition == "Thunderstorm":
            weather_icon = " "
        elif w_condition == "Snow":
            weather_icon = " "
        elif w_condition in [
            "Mist",
            "Smoke",
            "Haze",
            "Dust",
            "Fog",
            "Sand",
            "Dust",
            "Ash",
            "Squall",
            "Tornado",
        ]:
            weather_icon = " "
        print("%{T3}" + weather_icon + "%{T-}  " + w_temp + "  " + w_condition + " in " + w_city + ", " + w_country)

while True:
    full_music_title = (
        subprocess.run(TITLE_COMMAND.split(" "), capture_output=True)
        .stdout.decode("UTF-8")
        .replace("\n", "")
    )
    if len(full_music_title) > 30:
        music_title = full_music_title[:30] + "..."
    else:
        music_title = full_music_title
    music_artist = (
        subprocess.run(ARTIST_COMMAND.split(" "), capture_output=True)
        .stdout.decode("UTF-8")
        .replace("\n", "")
    )

    # Exit when no title
    if not full_music_title or not music_artist:
        print_weather()
        sleep(SLEEP_INTERVAL)
        continue

    # Logic to exclude certain programs
    for item in excluded_list:
        if item.lower() in full_music_title.lower():
            print_weather()
            sleep(SLEEP_INTERVAL)
            continue

    music_status = str(subprocess.run(STATUS_COMMAND.split(" "), capture_output=True))

    if STATUS_PLAY in music_status:
        output = "%{T3}" + ICON_TITLE + "%{T-}  " + music_artist + " - " + music_title + "  %{T3}%{A1:playerctl previous:}" + ICON_PREVIOUS + "%{A}  %{A1:playerctl play-pause:}" + ICON_PAUSE + "%{A}  %{A1:playerctl next:}" + ICON_NEXT + "%{A}%{T-}"
    elif STATUS_PAUSE in music_status:
        output = "%{T3}" + ICON_TITLE + "%{T-}  " + music_artist + " - " + music_title + "  %{T3}%{A1:playerctl previous:}" + ICON_PREVIOUS + "%{A}  %{A1:playerctl play-pause:}" + ICON_PLAY + "%{A}  %{A1:playerctl next:}" + ICON_NEXT + "%{A}%{T-}"
    print(output)
    sleep(SLEEP_INTERVAL)
