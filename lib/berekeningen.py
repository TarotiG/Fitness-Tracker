"""
Alle gegevens en berekeningen die benodigd zijn voor het berekenen van de caloriebehoeften
staan hier vermeld.
"""


class Berekeningen():
    """Attributen"""
    # Factor die de caloriebehoefte verhoogd op basis van wekelijkse beweging van de gebruiker
    pal_waarden = dict(licht=1.2, weinig=1.325, veel=1.55, zwaar=1.725, extreem=1.9)

    """Methoden"""
    # Berekent de BMR (Basic Metabolic Rate) van de gebruiker
    @staticmethod
    def bereken_bmr(obj) -> int:
        if obj.geslacht == 'Man':
            bmr = int(66.4730 + (13.7516 * obj.gewicht) + (5.0033 * obj.lengte) - (6.7550 * obj.leeftijd))
            return bmr
        elif obj.geslacht == 'Vrouw':
            bmr = int(655.0955 + (9.5634 * obj.gewicht) + (1.8496 * obj.lengte) - (4.6756 * obj.leeftijd))
            return bmr

    # Bepaalt welke factor nodig is voor de berekening van de caloriebehoefte op basis van de beweging per week
    @staticmethod
    def bepaal_pal_waarde(obj) -> float:

        for key in obj.pal_waarden:
            if obj.beweging_per_week == key:
                return obj.pal_waarden.get(key)

    # Calorie behoefte berekenen op basis van BMR en PAL waarde
    @staticmethod
    def bereken_calorie_behoefte(obj) -> int:
        calorie_behoefte = int(obj.bmr * Berekeningen.bepaal_pal_waarde(obj))
        return calorie_behoefte

    # Berekent het aantal calorieën dat nodig is om het doel te bepalen
    @staticmethod
    def bereken_calorie_doel(obj) -> list:
        calorie_doelen = []
        
        if obj.doel == "afvallen":
            calorie_doelen.append(obj.calorie_behoefte - 250)
            calorie_doelen.append(obj.calorie_behoefte - 500)
        
        elif obj.doel == "aankomen":
            calorie_doelen.append(obj.calorie_behoefte + 250)
            calorie_doelen.append(obj.calorie_behoefte + 500)
        
        return calorie_doelen

    @staticmethod
    def bereken_energie_gebruik_per_min(obj):
        """
        Formule:
        Energiegebruik per kcal/min = (MET-waarde * 3.5 * gewicht) / 200

        Bron MET tabel: google --> met-waarde tabel kngf
        """
        raise NotImplementedError("MET waarden nog ophalen")
