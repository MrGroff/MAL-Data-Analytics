import requests
import json
import time
from pathlib import Path
import sys
import re

line = "https://api.jikan.moe/v4/anime/43523/full"
anime = requests.get(line)
#print(anime.status_code)
anime = anime.json()
print(anime)