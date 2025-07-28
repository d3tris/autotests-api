import asyncio
import websockets


async def client():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        message = "Hello, server!"
        print(f"Sending: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Answer from server: {response}")


asyncio.run(client())
