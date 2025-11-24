"""
靜態網頁爬蟲練習
"""

import requests
from bs4 import BeautifulSoup
import json
from requests import get, post, put, delete

web = requests.get("https://water.taiwanstat.com/")
soup = BeautifulSoup(web.content, "html.parser")
reservoirs = soup.find_all("div", class_="reservoir")
for i in range(len(reservoirs)):
    name = reservoirs[i].find("div", class_="name").text.strip()
    volume_string = reservoirs[i].find("div", class_="volumn").text.strip()
    volume = float(volume_string.replace("萬立方公尺", ""))
    reservoirs[i] = {
        "name": name,
        "volume": volume
    }
with open("reservoirs.json", "w", encoding="utf-8") as f:
    json.dump(reservoirs, f, ensure_ascii=False)