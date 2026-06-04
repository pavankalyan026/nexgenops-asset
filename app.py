from fastapi import FastAPI
from database.db import engine
from database.models import Base

from routes.assets import router as asset_router
from routes.amc import router as amc_router

app = FastAPI(
    title="NexgenOps Asset"
)

Base.metadata.create_all(bind=engine)

app.include_router(asset_router)
app.include_router(amc_router)

@app.get("/")
def home():
    return {
        "application": "NexgenOps Asset",
        "version": "1.0"
    }