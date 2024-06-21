from gebruiker.gebruiker import Gebruiker
from gebruiker.gebruiker_profiel import GebruikerProfiel
from lib.berekeningen import Berekeningen
from workout.activiteit import Activiteit
from workout.workout import Workout
from workout.workout_split import WorkoutSplit
from workout.oefening import Oefening
from rapportage.rapportage import Rapportage
from logboek.logboek import Logboek


class WorkoutProfiel(GebruikerProfiel):
    """
    Class voor het opstellen van grafieken, rapportages en analyses op de workouts van de gebruiker. Dit is een childclass van GebruikerProfiel.
    Extra attributen zijn:
    - workout_splits: list[WorkoutSplit]
    - workouts: list[Workout]
    - logboek: Logboek
    """
    workout_splits: list[WorkoutSplit]
    workouts: list[Workout]
    logboek: Logboek
    
    def __init__(self, naam, geslacht, leeftijd, gewicht, lengte, beweging_per_week, doel, doel_gewicht,workout_splits, workouts):
        super().__init__(naam, geslacht, leeftijd, gewicht, lengte, beweging_per_week, doel, doel_gewicht)
        self.workout_splits = workout_splits
        self.workouts = workouts