from typing import List

from fastapi import WebSocket

from lucid.chat_agent import ChatAgent


class WebSocketManager:
    """Manage WebSocket Connections"""

    def __init__(self):
        """Initialize the WebSocketManager class"""
        self.chat_agent = ChatAgent()
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

    async def chat(self, message: str, websocket: WebSocket):
        """Chat with the agent-based message diff"""
        if self.chat_agent:
            response = self.chat_agent.chat(message)
            await websocket.send_json({"type": "chat", "content": response})
        else:
            await websocket.send_json(
                {
                    "type": "chat",
                    "content": "ChatAgent not avaliable",
                }
            )
