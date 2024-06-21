from dataclasses import dataclass
import datetime
from workout.activiteit import Activiteit
from workout.workout import Workout
from workout.workout_split import WorkoutSplit
from workout.oefening import Oefening


@dataclass
class Logboek:
    """
    Class voor het opstellen van het logboek. Het logboek houdt bij wat de gebruiker heeft uitgevoerd op een trainingsdag. De data is benodigd voor het opstellen van grafieken en rapportages.
    """
    datum: datetime.datetime
    dag_workout: list[Workout]
    oefeningen: list[Oefening]
    opmerkingen: list[str]