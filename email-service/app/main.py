from fastapi import FastAPI, Request

from .rabbitmq.run_manager import MessageQueueManager
from .email_sender import send_email


app = FastAPI()
mqtask = MessageQueueManager()

app.add_event_handler("startup", mqtask.start_messages_listener)
app.add_event_handler("shutdown", mqtask.stop_message_listener)

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