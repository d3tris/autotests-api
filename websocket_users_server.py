import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Received message from user: {message}")
        for _ in range(5):
            response = f"{_ + 1} User message: {message}"
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server running on ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
