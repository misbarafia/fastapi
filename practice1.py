from typing import Optional
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def first_api():
    return {'meaasge':  "Hello Misbah, Welcome to FAST API"}
