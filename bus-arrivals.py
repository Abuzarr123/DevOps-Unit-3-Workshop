import requests
import json
import sys
url = ('https://api.tfl.gov.uk/StopPoint/490012553B/Arrivals')

r = requests.get(url)
data = r.json()
if len(sys.argv) > 1:
    route_filter = sys.argv[1]
else:
    route_filter = input("Enter route number to filter (either 214 or 46) or press Enter for all: ")

for arrival in data:
    if not route_filter or arrival.get('lineName') == route_filter:
        print(f"Line: {arrival.get('lineId')}")
        print(f"Line Name: {arrival.get('lineName')}")
        print(f"Direction: {arrival.get('direction')}")
        print(f"Aimed Departure: {arrival.get('expectedArrival')}")
        print("-" * 50)

##print(json.dumps(r.json(), indent=2))