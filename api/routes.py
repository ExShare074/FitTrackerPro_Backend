from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from api.logic.database import (
    start_cycle, get_today_workout, complete_today,
    get_status, user_exists, is_completed,
    add_calories, get_today_calories, get_week_calories,
    add_weight, get_weight_history
)

router = APIRouter()

feedback_storage = []

class StartCycleRequest(BaseModel):
    username: str
    weeks: int
    split: int

class UsernameRequest(BaseModel):
    username: str

class CaloriesRequest(BaseModel):
    username: str
    product: str
    protein: int
    fat: int
    carbs: int
    kcal: int

class FeedbackRequest(BaseModel):
    username: str
    message: str

class WeightRequest(BaseModel):
    username: str
    kg: float

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
    add_calories(
        data.username,
        data.product,
        data.protein,
        data.fat,
        data.carbs,
        data.kcal
    )
    return {"status": "added"}

@router.get("/api/calories/today")
def get_user_calories(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return get_today_calories(username)

@router.get("/api/calories/week")
def get_user_week_calories(username: str, offset: int = Query(0)):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return get_week_calories(username, offset)

@router.post("/api/feedback")
def submit_feedback(data: FeedbackRequest):
    feedback_storage.append({"username": data.username, "message": data.message})
    return {"status": "feedback received"}

@router.post("/api/weight")
def save_weight(data: WeightRequest):
    if not user_exists(data.username):
        raise HTTPException(status_code=404, detail="User not found")
    add_weight(data.username, data.kg)
    return {"status": "weight saved"}

@router.get("/api/weight")
def get_weight(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return get_weight_history(username)

@router.get("/api/progress")
def get_progress(username: str):
    if not user_exists(username):
        raise HTTPException(status_code=404, detail="User not found")
    return users[username]["plan"].get_progress()