import websocket
import json
import requests
import re

# Define headers for requests
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch values using regex from a given URL
def fetch_value(url, pattern):
    response = requests.get(url, headers=headers)
    match = re.search(pattern, response.text)
    if match:
        return int(match.group(1))
    else:
        return None

# Calculate the percentage of removed hit points to base hit points
def calculate_percentage(url):
    base = fetch_value(url, r'"baseHitPoints"\s*:\s*(\d+)')
    removed = fetch_value(url, r'"removedHitPoints"\s*:\s*(\d+)')
    if not removed and base:
        return 0
    elif base and removed:
        return removed / base
    else:
        return None

# WebSocket event handlers
def on_message(ws, message):
    print("Received:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("### WebSocket Closed ###")

def on_open(ws, sources, filter_name, character_id):
    url = f"https://character-service.dndbeyond.com/character/v5/character/{character_id}"
    percentage = calculate_percentage(url)
    

    def send_filter_settings():
        if percentage is not None:
            set_filter_settings_command = {
                "op": 6,
                "d": {
                    "requestId": 2,
                    "requestType": "SetSourceFilterSettings",
                    "requestData": {
                        "sourceName": sources,
                        "filterName": filter_name,
                        "filterSettings": {"opacity": percentage}
                    }
                }
            }
            ws.send(json.dumps(set_filter_settings_command))

    print("WebSocket Opened")
    ws.send(json.dumps({
        "op": 1,
        "d": {
            "rpcVersion": 1,
            "authentication": None
        }
    }))
    send_filter_settings()
    while True:
        new_percentage = calculate_percentage(url)
        if percentage != new_percentage:
            percentage = new_percentage
            send_filter_settings()

def start_websocket(ws_url, sources, filter_name, character_id):
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=lambda ws: on_open(ws, sources, filter_name, character_id))
    ws.run_forever()
