from fastapi import FastAPI, dependencies, Depends, requests, Request
from pydantic import BaseModel

from .config import Config
from .db import connect_and_init_db, close_db_connection, get_db_client


app = FastAPI()

app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connection)


@app.get("/")
def read_root():
    return {"Hello": "World"}
