from fastapi import FastAPI
from app.db import database, metadata, engine
from app.api.sample import router as sample_router

app = FastAPI(title="FastAPI meetup")


@app.get("/")
def read_root():
    return {"hello": "devs"}


app.include_router(sample_router, prefix="/sample", tags=["sample"])


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
        # metadata.drop_all(engine)
        metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
