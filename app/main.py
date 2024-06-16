from gebruiker.gebruiker import Gebruiker
from gebruiker.gebruiker_profiel import GebruikerProfiel
from lib.berekeningen import Berekeningen


def main():
    """Main applicatie"""
    leestekens = '"~`!@#$%^&*()_+-={}[]:;<>?,./|'
    
    # test gebruiker
    print("Wat voor workout split heb je?")
    splits = [x for x in input().split()]
    
    tyron = GebruikerProfiel('Tyron Gysbertha', 'Man', 29, 98, 180, 'zwaar', 'afvallen', 90)
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
    Workout split:
    - {splits[0].strip(leestekens)}
    - {splits[1].strip(leestekens)}
    - {splits[2].strip(leestekens)}
    
    VOORBEELD
    Split 1:
    - Oefening 1
    - Oefening 2
    - Oefening 3
    Split 2:
      etc.
    
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