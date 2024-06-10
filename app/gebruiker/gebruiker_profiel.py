from gebruiker.gebruiker import Gebruiker
from lib.berekeningen import Berekeningen


class GebruikerProfiel(Gebruiker, Berekeningen):
    """
    Class voor het profiel/data van de gebruiker
    """
    naam: str = ''
    geslacht: str = ''
    leeftijd: int = 0
    email_adres: str = ''
    gewicht: float = 0
    lengte: float = 0
    bmr: int = 0
    calorie_behoefte: int = 0
    beweging_per_week: str = ''
    doel: str = ''
    doel_gewicht: int = 0
    calorie_doel: list[int] = []

    def __init__(self, naam, geslacht, leeftijd, gewicht, lengte, beweging_per_week, doel, doel_gewicht):
        self.naam = naam
        self.geslacht = geslacht
        self.leeftijd = leeftijd
        self.gewicht = gewicht
        self.lengte = lengte
        self.beweging_per_week = beweging_per_week.lower()
        self.doel = doel
        self.doel_gewicht = doel_gewicht

        # BMR berekenen bij aanmaak Gebruiker
        self.bmr = Berekeningen.bereken_bmr(self)

        # Calorie behoefte berekenen bij aanmaak Gebruiker
        self.calorie_behoefte = Berekeningen.bereken_calorie_behoefte(self)

        # Calorieën gewichtsdoel berekenen
        self.calorie_doel = Berekeningen.bereken_calorie_doel(self)

    # Berekent de BMR (Basic Metabolic Rate) van de gebruiker
    def berekening_bmr(self):
        if self.geslacht == 'Man':
            self.bmr = int(66.4730 + (13.7516 * self.gewicht) + (5.0033 * self.lengte) - (6.7550 * self.leeftijd))
            return self.bmr
        elif self.geslacht == 'Vrouw':
            self.bmr = int(655.0955 + (9.5634 * self.gewicht) + (1.8496 * self.lengte) - (4.6756 * self.leeftijd))
            return self.bmr