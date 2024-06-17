from gebruiker.gebruiker import Gebruiker
from gebruiker.gebruiker_profiel import GebruikerProfiel
from lib.berekeningen import Berekeningen
from workout.activiteit import Activiteit
from workout.workout import Workout
from workout.workout_profiel import WorkoutProfiel
import datetime
import random


def main():
    """Main applicatie"""
    # leestekens = '"~`!@#$%^&*()_+-={}[]:;<>?,./|'
    spiergroepen = ["Borst", "Rug", "Benen", "Armen", "Cardio"]

    splits = [
        "Borst",
        "Rug",
        "Benen",
        "Cardio"
    ]
    workouts = []
    for i in range(10):
        workout = Workout(random.randint(1, 100), datetime.datetime.now(), random.choice(spiergroepen), ["Oefening 1", "Oefening 2", "Oefening 3"])
        workouts.append(workout)
    
    # test gebruiker voor data
    tyron = WorkoutProfiel('Tyron Gysbertha', 'Man', 29, 98, 180, 'zwaar', 'afvallen', 90, splits, workouts)
    
    print(f"""
    Persoonsgegevens
    Naam:               {tyron.naam}
    Geslacht:           {tyron.geslacht}
    Leeftijd:           {tyron.leeftijd}
    Gewicht:            {tyron.gewicht} kg
    Lengte:             {tyron.lengte} cm

    Gezondheidsmeter
    BMR:                         {tyron.bmr} Kcal
    Beweging per week:           {tyron.beweging_per_week}
    Doel gewicht:                {tyron.doel_gewicht} kg
    
    Caloriebehoefte:             {tyron.calorie_behoefte} Kcal (Maintenance)
    Caloriebehoefte obv doel:    {tyron.calorie_doel[0]} Kcal (Aangeraden hoeveelheid)
    Caloriebehoefte obv doel:    {tyron.calorie_doel[1]} Kcal (Uiterste grens)

    Beweging
    Workout split: {random.choice(splits)}
    
    Workout:
    Spiergroep: {tyron.workouts[0].spier_groep}
    Oefeningen voor deze spiergroep:
    - {tyron.workouts[0].oefeningen[0]}
    - {tyron.workouts[0].oefeningen[1]}
    - {tyron.workouts[0].oefeningen[2]}
    
    Voortgang
    Gewicht:
    UITWERKEN
    
    Kracht:
    UITWERKEN

    Voeding:
    UITWERKEN
    
    """)

if __name__ == "__main__":
    main()