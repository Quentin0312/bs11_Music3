import os
from fastapi import WebSocket


# TODO: Find a cleaner way to do
def is_connection_authorized(websocket: WebSocket) -> bool:
    if websocket.headers.get("origin") == os.environ.get("FRONTURL"):
        return True
    else:
        print("Unauthorized access => ", websocket.headers.get("origin"))
        return False