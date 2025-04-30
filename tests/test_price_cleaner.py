import unittest #framework de pruebas unitarias para Python
from utils.price_cleaner import limpiar_precio


class TestPrecioCleaner(unittest.TestCase):
    #assertEqual indica que esa es una prueba que debe pasar el código que se escribió
    #se debe cumplir una igualdad en los resultados
    def test_precio_normal(self):
        self.assertEqual(limpiar_precio('COP $740 113.22'), 740113.22)

    def test_precio_con_descuento(self):
        self.assertEqual(limpiar_precio('$1.530.000\n15% OFF'), 1530000.0)

    def test_precio_europeo(self):
        self.assertEqual(limpiar_precio('COP897.205,6'), 897205.6)

    def test_precio_vacio(self):
        self.assertIsNone(limpiar_precio(''))

if __name__ == '__main__':
    unittest.main()
