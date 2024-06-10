from gebruiker.gebruiker import Gebruiker
from gebruiker.gebruiker_profiel import GebruikerProfiel
from lib.berekeningen import Berekeningen


def main():
    """Main applicatie"""
    
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
    
    VOORBEELD
    Split 1:
    - Oefening 1
    - Oefening 2
    - Oefening 3
    Split 2:
      etc.
    
    
    """)

if __name__ == "__main__":
    main()