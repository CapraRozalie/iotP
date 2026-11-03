import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOLEMIO_API_KEY")

if not API_KEY:
    raise ValueError("GOLEMIO_API_KEY not found in .env")

url = "https://api.golemio.cz/v2/sortedwastestations"

headers = {
    "X-Access-Token": API_KEY,
    "Accept": "application/json"
}

params = {
    "latlng": "50.124935,14.457204",
    "range": 5000,
    "onlyMonitored": "true",
    "limit": 10,
    "offset": 0
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=30
)

print("Status:", response.status_code)

response.raise_for_status()

data = response.json()

# Save results to JSON
with open("../../waste_stations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

features = data.get("features", [])

print("Number of stations:", len(features))

for feature in features:
    print(feature.get("properties", {}))