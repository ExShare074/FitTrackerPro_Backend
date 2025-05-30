from typing import Dict

# Временное хранилище пользователей
users: Dict[str, Dict] = {}


def start_cycle(username: str, weeks: int, split: int):
    from api.logic.workout import WorkoutPlan
    users[username] = {
        "plan": WorkoutPlan(weeks, split)
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