from activiteit import Activiteit
from dataclasses import dataclass


@dataclass
class Oefening(Activiteit):
    id: int
    naam_oefening: str
    aantal_sets: int
    aantal_herhalingen: int
    rust_tijd_per_set: int
