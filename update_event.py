import requests
from datetime import datetime

URL = "https://www.scorebat.com/video-api/v3/feed/?token=MzYxMTZfMTcwNjA2MTk3OV8yY2QxOWY3N2JhY2M5ZWU2NDVlZGIwNGU0MTEwMzE3MzA2NzEwMTU%3D"

try:
    r = requests.get(URL, timeout=10)
    data = r.json()
except:
    data = {"response": []}

today = datetime.utcnow().date()

m3u = "#EXTM3U\n"

for match in data.get("response", []):
    try:
        match_date = datetime.fromisoformat(match["date"].replace("Z", "")).date()
        title = match["title"]
    except:
        continue

    if match_date == today:
        m3u += f'#EXTINF:-1 group-title="LIVE EVENT", {title}\n'
        m3u += "http://0.0.0.0/stream.m3u8\n\n"

with open("event.m3u", "w") as f:
    f.write(m3u)
