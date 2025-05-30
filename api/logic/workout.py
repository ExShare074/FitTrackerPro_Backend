from typing import List, Dict

class WorkoutPlan:
    def __init__(self, weeks: int = 8, split_days: int = 3):
        self.weeks = weeks
        self.split_days = split_days
        self.current_week = 1
        self.current_day = 1
        self.plan = self.generate_plan()

    def generate_plan(self) -> Dict[int, Dict[int, List[str]]]:
        plan = {}
        for week in range(1, self.weeks + 1):
            plan[week] = {}
            for day in range(1, self.split_days + 1):
                plan[week][day] = [f"Exercise {i+1}" for i in range(4)]
        return plan

    def get_today_workout(self) -> List[str]:
        return self.plan[self.current_week][self.current_day]

    def complete_today(self):
        if self.current_day < self.split_days:
            self.current_day += 1
        else:
            self.current_day = 1
            self.current_week += 1

    def is_completed(self) -> bool:
        return self.current_week > self.weeks

    def get_status(self):
        return {
            "week": self.current_week,
            "day": self.current_day,
            "total_weeks": self.weeks
        }