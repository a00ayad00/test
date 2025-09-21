from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    html_content = """
        <html>
            <head>
                <title>Smart Vision API</title>
            </head>
            <body>
                <h1>
                    Welcome to Smart Vision API
                </h1>
                <h2>
                The current available endpoints are:
                </h2>
                <h3>
                    <ul>
                        <li> Smart Vision </li>
                        <li> Clothes Image Classification </li>
                        <li> Object Counting </li>
                        <li> Streaming camera (simple) </li>
                        <li> VQA (MoonDream model) </li>
                        <li> Rased for Construction Process </li>
                        <li> Chooch.ai endpoints </li>
                    </ul>
                </h3>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

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

    uvicorn.run("test:app", host="0.0.0.0", port=8000)

