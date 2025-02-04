from fastapi import FastAPI

from .db import connect_and_init_db, close_db_connection, get_db_client
from .message_queue import start_message_listener


app = FastAPI()

app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connection)
app.add_event_handler("startup", start_message_listener)


@app.get("/")
async def root():
    return {"status": "ok"}
