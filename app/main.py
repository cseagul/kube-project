from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API Fetch Service")

app.include_router(router)