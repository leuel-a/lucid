from typing import List

from fastapi import WebSocket


class WebSocketManager:
    """Manage WebSocket Connections"""

    def __init__(self):
        """Initialize the WebSocketManager class"""
        self.chat_agent = None
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Connect a new WebSocket client"""
        try:
            await websocket.accept()
            self.active_connections.append(websocket)
        except Exception as e:
            print(f"Error connecting websocket: {e}")
            if websocket in self.active_connections:
                await self.disconnect(websocket)

    async def disconnect(self, websocket: WebSocket):
        """Disconnect a WebSocket client"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

            try:
                await websocket.close()
            except:
                pass  # Connection might already be closed

    async def chat(self, _, websocket: WebSocket):
        """Chat with the agent-based message diff"""
        if self.chat_agent:  # call the chat agent when the agent is avaliable
            pass
        else:
            await websocket.send_json(
                {
                    "type": "chat",
                    "content": "Knowledge empty, please run the research first to obtain knowledge",
                }
            )
