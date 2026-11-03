import json
import os
import requests

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NjY4MSwiaWF0IjoxNzkzNzM3NjIzLCJleHAiOjExNzkzNzM3NjIzLCJpc3MiOiJnb2xlbWlvIiwianRpIjoiNmYxOGE1OTctNmZhZi00NjkyLTg1NWEtOTBhZmQwZWRkMjY4In0.EzwGty0TlSjWa_qlVFr_NHpIcWIuenXT6XoS_hBibG4"

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

# Display number of stations
features = data.get("features", [])

print("Number of stations:", len(features))

# Display station properties
for feature in features:
    print(feature.get("properties", {}))
