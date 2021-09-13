#!/usr/bin/env python
import os
import requests as http
from collections import Counter

raw_contents = []
urls_to_fetch = []
teams = []
url_format = 'https://raw.githubusercontent.com/{}/mylab2/main/test.txt'

def fetch(filename: str):
    with open(name, mode='r') as f:
        song = f.readline()
        if not song.rstrip():
            song = f.readline()
        
        f.readline()
        url_to_repo = f.readline()
        return (song, url_to_repo.split('/')[3])

for root, dirs, files in os.walk("."):
    for name in files:
        if ".txt" in name:
            raw_contents.append(fetch(name))

print("Songs:\n======")
for song in raw_contents:
    print(f"{song[0].rstrip()} ({song[1]})")
    urls_to_fetch.append(url_format.format(song[1]))

print("\n")

for url in urls_to_fetch:
    res = http.get(url)
    if res.status_code == 404:
        continue

    teams.append(res.text.rstrip())

for counted in Counter(teams).most_common():
    print(f"{counted[0]} {counted[1]}")
