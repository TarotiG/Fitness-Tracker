"""
Workout splits worden hier gedefinieerd.

Voorbeelden zijn:
- Borst, Rug, Benen, Armen
- Push, Pull, Benen
- Full body

"""
from dataclasses import dataclass
from workout.workout import Workout


@dataclass
class WorkoutSplit(Workout):
    def __init__(self):
        raise NotImplementedError("Nog uitwerken")