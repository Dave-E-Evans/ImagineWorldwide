# Uses the Countly API spec to send an event
import datetime
import json
import requests
from urllib.parse import quote

# Encode some information about events 
events = [
    {
        "key": "level_success",
        "count": 4
    },
    {
        "key": "level_fail",
        "count": 2
    }
]

events_as_string = json.dumps(events)
events_as_url_encoded_string = quote(events_as_string)

# Generate now as a timestamp YYYY-MM-DD
now = datetime.datetime.utcnow().timestamp()
now_as_string = datetime.datetime.utcfromtimestamp(now).strftime('%Y-%m-%d')

url = "http://127.0.0.1:3000/i?app_key=app_key&device_id=device_id&timestamp=" + now_as_string + "&events=" + events_as_url_encoded_string
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)