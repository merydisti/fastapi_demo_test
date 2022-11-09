from fastapi import FastAPI
from app.db import database, metadata, engine
from app.api.users import router as users_router
from app.api.products import router as products_router

app = FastAPI(title="FastAPI meetup")


@app.get("/")
def read_root():
    return {"hello": "devs"}


app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(products_router, prefix="/products", tags=["products"])


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
