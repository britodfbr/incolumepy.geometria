from unittest import TestCase
from incolumepy.geometria.triangulo import Triangulo

class TestQuadrado(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.fig = Triangulo()

    def test_get_area(self):
        # Verificamos se o resultado é o esperado
        # de acordo com a formula de area do quadrado
        self.fig.base = 2
        self.fig.altura = 7.0
        self.assertEqual(self.fig.get_area(), 14.)

        self.fig.base = 7
        self.fig.altura = 7.0
        self.assertEqual(self.fig.get_area(), 49.0)

    def test_get_perimetro(self):
        self.fig.lados = [2,3,5]
        self.assertEqual(self.fig.get_perimetro(), 10)
        self.fig.lados = [12, 15, 19]
        self.assertEqual(self.fig.get_perimetro(), 46.0)