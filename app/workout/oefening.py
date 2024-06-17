from workout.activiteit import Activiteit
from dataclasses import dataclass


@dataclass
class Oefening(Activiteit):
    """Class om een type oefening te definiëren.
    Beschrijving van de attributen:
    - id: Id van de oefening.
    - naam_oefening: Naam van de oefening.
    - spier_groep: Bepaling spiergroep. Key voor WorkoutSplit.
    - type_oefening: Bepaling van de type (Kracht/Cardio/etc.)
    - aantal_sets: Aantal sets.
    - aantal_herhalingen: Aantal herhalingen.
    - rust_tijd_per_set: Tijd tussen sets in seconden.
    """
    id: int
    naam_oefening: str
    spier_groep: str
    type_oefening: str
    aantal_sets: int
    aantal_herhalingen: int
    rust_tijd_per_set: int
