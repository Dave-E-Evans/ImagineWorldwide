# Uses the Countly API spec to send an event
import datetime
import json
import os
import requests
from urllib.parse import quote

# This is the Countly host that the client will connect to.
countly_host = os.environ.get('COUNTLY_HOST', '127.0.0.1')
countly_port = int(os.environ.get('COUNTLY_PORT', '3000'))

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

url = f"http://{countly_host}:{countly_port}/i?app_key=app_key&device_id=device_id&timestamp={now_as_string}&events={events_as_url_encoded_string}"
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)