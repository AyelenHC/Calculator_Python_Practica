import unittest 
from app.logica.calculator import Calculator

# Aprendiendo a realizar las pruebas unitarias en python --> Para ejecutar esta prueba: python -m unittest discover tests

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # numbers natural
    def test_add_positives(self):
        result = self.calc.add(5, 20)
        assert result == 25

    def test_add_negatives(self):
        result = self.calc.add(-15, -30)
        assert result == -45

    def test_add_mixed(self):
        result = self.calc.add(8, -8)
        assert result == 0

    # float numbers
    def test_add_positives_float(self):
        result = self.calc.add(5.8, 20.9)
        assert result == 26.7

    def test_add_negatives_float(self):
        result = self.calc.add(-15.05, -30.09)
        assert result == -45.14

    def test_add_mixed_float(self):
        result = self.calc.add(8.01, -8.05)
        assert result == -0.04