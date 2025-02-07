from fastapi import FastAPI, Request

from .message_queue import start_messages_saver
from .email_sender import send_email


app = FastAPI()

app.add_event_handler("startup", start_messages_saver)

@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/email")
async def send(request: Request):
    import json
    data = await request.body()
    data = json.loads(data)
    await send_email(data=data)

    return {"status": "ok"}