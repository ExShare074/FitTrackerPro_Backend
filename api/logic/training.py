from typing import List, Dict

class Day:
    def __init__(self, exercises: Dict[str, float]):
        self.exercises = exercises

class Week:
    def __init__(self, days: List[Day]):
        self.days = days

class TrainingCycle:
    def __init__(self, weeks: List[Week]):
        self.weeks = weeks

KEY_EXERCISES = [
    "Приседания со штангой",
    "Жим ногами",
    "Жим штанги лежа",
    "Жим гантелей лежа",
    "Тяга штанги в наклоне"
]

DEFAULT_EXERCISES = KEY_EXERCISES + ["Тяга блока", "Подъем на бицепс", "Планка"]


def generate_training_program(duration_weeks: int, base_weights: Dict[str, float]) -> TrainingCycle:
    weeks = []
    for week_index in range(duration_weeks):
        days = []
        for _ in range(3):  # 3 тренировки в неделю
            exercises = {}
            for name in DEFAULT_EXERCISES:
                base = base_weights.get(name, 20.0)
                if name in KEY_EXERCISES:
                    if week_index < duration_weeks // 2:
                        increment = 5.0
                    else:
                        increment = 2.5
                else:
                    increment = 2.5
                weight = round(base + increment * week_index, 1)
                exercises[name] = weight
            days.append(Day(exercises=exercises))
        weeks.append(Week(days=days))
    return TrainingCycle(weeks=weeks)


def calculate_progression(start_weight: float, weeks: int) -> List[float]:
    return [start_weight + i * 2.5 for i in range(weeks)]
