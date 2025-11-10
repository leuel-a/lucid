import json

from fastapi import WebSocket, WebSocketDisconnect

from websocket_manager import WebSocketManager


async def handle_websocket_communication(websocket: WebSocket, manager: WebSocketManager):
    """Handles WebSocket Communication"""
    while True:
        try:
            data = await websocket.receive_text()

            if data == "ping":
                await websocket.send_text("pong")
            elif data.startswith("chat"):
                await handle_chat(websocket, data, manager)
            else:
                print("Error: Unknown command or not enough parameters provided.")
        except WebSocketDisconnect:
            print("INFO:\t  WebSocket Disconnected Cleanly.")
            break
        except Exception as e:
            print(f"WebSocket error: {e}")
            break


async def handle_chat(websocket: WebSocket, data: str, manager: WebSocketManager):
    json_data = json.loads(data[4:])
    print(f"INFO:\t  Received Chat Message:  {json_data.get('message')}")
    await manager.chat(json_data.get("message"), websocket)
