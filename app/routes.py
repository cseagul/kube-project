from fastapi import APIRouter
from app.service import fetch_data

router = APIRouter()

@router.get("/")
def health():
    return {"ok", "hello world"}

@router.get("/data")
def get_data():
    return fetch_data()


@router.get("/health")
def health():
    return {"status": "ok"}

