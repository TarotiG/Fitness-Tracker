from workout.activiteit import Activiteit
from workout.oefening import Oefening
import datetime


class Workout(Activiteit):
    id: int
    workout_datum: datetime.datetime
    workout_split: list[str]
    oefeningen: list[Oefening]
    totale_tijd: int
    calorieen_verbrand: int

    def get_oefeningen(self):
        raise NotImplementedError("Specs uitschrijven")

    def get_workout_splits(self):
        raise NotImplementedError("Specs uitschrijven")