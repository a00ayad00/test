from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
import uvicorn

app = FastAPI()


@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}


if __name__ == "__main__":
    # test_websocket()
    uvicorn.run("test:app", host="0.0.0.0", port=6000, reload=True)