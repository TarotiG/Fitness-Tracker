from gebruiker.gebruiker_profiel import GebruikerProfiel


def main():
    """Main applicatie"""
    
    tyron = GebruikerProfiel('Tyron Gysbertha', 'Man', 29, 98, 180, 'zwaar', 'afvallen', 90)
    print(f"""
    Naam:               {tyron.naam}
    Geslacht:           {tyron.geslacht}
    Leeftijd:           {tyron.leeftijd}
    Gewicht:            {tyron.gewicht} kg
    Lengte:             {tyron.lengte} cm

    BMR:                {tyron.bmr} Kcal
    Caloriebehoefte:    {tyron.calorie_behoefte} Kcal (Maintenance)
    
    Caloriebehoefte obv doel:    {tyron.calorie_doel[0]} Kcal (Aangeraden hoeveelheid)
    Caloriebehoefte obv doel:    {tyron.calorie_doel[1]} Kcal (Uiterste grens)
    """)

if __name__ == "__main__":
    main()