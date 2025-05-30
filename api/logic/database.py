from typing import Dict, List
from datetime import date

# Временное хранилище пользователей
users: Dict[str, Dict] = {}


def start_cycle(username: str, weeks: int, split: int):
    from api.logic.workout import WorkoutPlan
    users[username] = {
        "plan": WorkoutPlan(weeks, split),
        "calories": {}
    }


def get_today_workout(username: str):
    return users[username]["plan"].get_today_workout()


def complete_today(username: str):
    users[username]["plan"].complete_today()


def get_status(username: str):
    return users[username]["plan"].get_status()


def user_exists(username: str) -> bool:
    return username in users


def is_completed(username: str):
    return users[username]["plan"].is_completed()

# ==== КАЛОРИИ ====

def add_calories(username: str, product: str, kcal: int):
    today = str(date.today())
    user = users[username]
    if today not in user["calories"]:
        user["calories"][today] = []
    user["calories"][today].append({"product": product, "kcal": kcal})


def get_today_calories(username: str):
    today = str(date.today())
    entries = users[username]["calories"].get(today, [])
    total = sum(e["kcal"] for e in entries)
    return {"total": total, "entries": entries}