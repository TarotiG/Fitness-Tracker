from dataclasses import dataclass
from workout.workout import Workout
from workout.oefening import Oefening


@dataclass
class WorkoutSplit(Workout):
    """
    Workout splits worden hier gedefinieerd.

    Voorbeelden zijn:
    - Borst, Rug, Benen, Armen
    - Push, Pull, Benen
    - Full body

    """
    splits: list[str]
    aantal_dagen: int
    oefeningen: list[Oefening]
    
    def __init__(self):
        raise NotImplementedError("Nog uitwerken")