from fastapi import FastAPI

from .db import connect_and_init_db, close_db_connection, get_db_client
from .message_queue import start_messages_saver
from .resources.logs import router as logs_router

app = FastAPI()

app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connection)
app.add_event_handler("startup", start_messages_saver)
app.include_router(logs_router)

@app.get("/")
async def root():
    return {"status": "ok"}
