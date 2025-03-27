# modules/Strategie.py

class Strategie:
    def __init__(self, progression_ratio=0.5):
        self.progression_ratio = progression_ratio

    def calculer_lots(self, capital, nombre_ordres):
        """
        Calcule la répartition du capital en lots 
        selon la progression géométrique définie.
        """
        # Exemple simplifié
        lots = []
        ratio_courant = self.progression_ratio
        for i in range(nombre_ordres):
            part = capital * ratio_courant
            lots.append(part)
            ratio_courant *= self.progression_ratio
        return lots


if __name__ == "__main__":
    strat = Strategie(0.5)
    result = strat.calculer_lots(capital=1000, nombre_ordres=5)
    print("Lots calculés :", result)
