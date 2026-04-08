import requests
import json
import os
import time
from datetime import datetime

headers = {"User-Agent": "TrendPulse/1.0"}

TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "champsionship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    t = title.lower()
    for category in categories:
        for word in categories[category]:
            if word in t:
                return category
    return None

try:
    response = requests.get(TOP_URL, headers=headers)
    ids = response.json()[:500]
except:
    print("Error fetching top stories")
    ids = []

results = []
count = {c:0 for c in categories}

for i in ids:
    try:
        r = requests.get(ITEM_URL.format(i), headers=headers)
        story = r.json()

        if story is None:
            continue

        title = story.get("title","")
        category = get_category(title)

        if category is None:
            continue

        if count[category] >= 25:
            continue

        data = {
            "post_id": story.get("id"),
            "title": title.strip(),
            "category": category,
            "score": story.get("score",0),
            "num_comments": story.get("descendants",0),
            "author": story.get("by",""),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        results.append(data)
        count[category]+=1

        if all(count[c]>=25 for c in count):
            break

    except:
        print("Error fetching story", i)

for c in categories:
    time.sleep(2)

if not os.path.exists("data"):
    os.makedirs("data")

filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(filename,"w",encoding="utf-8") as f:
    json.dump(results,f,indent=4)

print("Collected",len(results),"stories. Saved to",filename)