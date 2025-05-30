from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.logic.database import (
    start_cycle, get_today_workout, complete_today,
    get_status, user_exists, is_completed,
    add_calories, get_today_calories
)

router = APIRouter()

class StartCycleRequest(BaseModel):
    username: str
    weeks: int
    split: int

class UsernameRequest(BaseModel):
    username: str

class CaloriesRequest(BaseModel):
    username: str
    product: str
    kcal: int

@router.get("/api/ping")
def ping():
    return {"message": "pong"}

@router.post("/api/start_cycle")
def start_new_cycle(data: StartCycleRequest):
    start_cycle(data.username, data.weeks, data.split)
    return {"status": "cycle started"}

@router.get("/api/workout")
def get_workout(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return {"workout": get_today_workout(username)}

@router.post("/api/complete_workout")
def complete_workout(data: UsernameRequest):
    if not user_exists(data.username):
        raise HTTPException(status_code=404, detail="User not found")
    complete_today(data.username)
    return {"status": "completed"}

@router.get("/api/status")
def get_user_status(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return get_status(username)

@router.get("/api/completed")
def check_completed(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return {"completed": is_completed(username)}

@router.post("/api/calories")
def add_user_calories(data: CaloriesRequest):
    if not user_exists(data.username):
        raise HTTPException(status_code=404, detail="User not found")
    add_calories(data.username, data.product, data.kcal)
    return {"status": "added"}

@router.get("/api/calories/today")
def get_user_calories(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return get_today_calories(username)