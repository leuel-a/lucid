#!/usr/bin/env python

import os
import logging

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from server_utils import handle_websocket_communication
from websocket_manager import WebSocketManager

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")

app = FastAPI()
logger = logging.getLogger(__name__)
manager = WebSocketManager()


@app.get("/healthcheck")
async def healthcheck():
    return {"status": True}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        await handle_websocket_communication(websocket, manager)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        logger.info("Websocket disconnected")


if __name__ == "__main__":
    uvicorn.run("server:app", host=HOST, port=8000, reload=True)
