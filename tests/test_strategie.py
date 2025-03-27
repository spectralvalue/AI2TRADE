import unittest
from modules.Strategie import Strategie

class TestStrategie(unittest.TestCase):
    def test_calculer_lots(self):
        strat = Strategie(progression_ratio=0.5)
        lots = strat.calculer_lots(capital=1000, nombre_ordres=5)
        self.assertEqual(len(lots), 5)
        # On peut vérifier qu'on a bien des valeurs décroissantes
        self.assertTrue(all(lots[i] >= lots[i+1] for i in range(len(lots)-1)))

if __name__ == '__main__':
    unittest.main()
