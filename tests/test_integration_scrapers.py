import unittest
from scraper import obtener_productos_amazon, obtener_productos_ebay, obtener_productos_aliexpress, obtener_productos_mercadolibre

class TestIntegrationScrapers(unittest.TestCase):

    def test_obtener_productos_amazon(self):
        url = "https://www.amazon.com/s?k=usb"
        productos = obtener_productos_amazon(url)
        self.assertIsInstance(productos, list) #se verifica que devuelva una lista de productos
        self.assertGreater(len(productos), 0) #y que contenga al menos 1 productos

    def test_obtener_productos_ebay(self):
        url = "https://www.ebay.com/sch/i.html?_nkw=usb"
        productos = obtener_productos_ebay(url)
        self.assertIsInstance(productos, list)
        self.assertGreater(len(productos), 0)

    def test_obtener_productos_aliexpress(self):
        url = "https://es.aliexpress.com/w/wholesale-usb.html"
        productos = obtener_productos_aliexpress(url)
        self.assertIsInstance(productos, list)
        self.assertGreater(len(productos), 0)

    def test_obtener_productos_mercadolibre(self):
        url = "https://articulo.mercadolibre.com.co/MLC624376091"
        productos = obtener_productos_mercadolibre(url)
        self.assertIsInstance(productos, list)
        self.assertGreater(len(productos), 0)

if __name__ == "__main__":
    unittest.main()
