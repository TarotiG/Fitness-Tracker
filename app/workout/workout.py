from workout.oefening import Oefening
import datetime


class Workout:
    id: int
    workout_datum: datetime.datetime
    spier_groep: str
    oefeningen: list[Oefening]
    totale_tijd: int
    calorieen_verbrand: int

    def __init__(self, id, workout_datum, spier_groep, oefeningen):
        self.id = id
        self.workout_datum = workout_datum
        self.spier_groep = spier_groep
        self.oefeningen = oefeningen
        

    def get_oefeningen(self):
        raise NotImplementedError("Specs uitschrijven")

    def get_workout_splits(self):
        raise NotImplementedError("Specs uitschrijven")
