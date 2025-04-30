import unittest
import os #permite que Python trabaje directamente con carpetas, archivos y rutas en tu computadora
import pandas as pd
from utils.exporter import exportar_a_excel


class TestExporter(unittest.TestCase):

    def setUp(self):
        #se proponen datos de prueba
        self.datos_prueba = [
            {"nombre": "Producto 1", "precio": 1000},
            {"nombre": "Producto 2", "precio": 2000}
        ]
        self.nombre_archivo = "test_productos.xlsx"

    def test_exportar_crear_archivo(self):
        #se ejecuta la función
        exportar_a_excel(self.datos_prueba, self.nombre_archivo)

        #busca la carpeta data, forma una ruta y a eso se le adiciona el nombre del archivo
        ruta_data = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "data")
        ruta_archivo = os.path.join(ruta_data, self.nombre_archivo)

        #verifica que el archivo si haya sido creado en la ruta de "data"
        self.assertTrue(os.path.exists(ruta_archivo), "El archivo no fue creado")

        #verificamos que el contenido sea correcto
        df = pd.read_excel(ruta_archivo, engine='openpyxl')
        self.assertEqual(len(df), 2)#cantidad de datos
        self.assertIn('nombre', df.columns)#títulos de las columnas
        self.assertIn('precio', df.columns)
        self.assertEqual(df.iloc[0]['nombre'], 'Producto 1')
        self.assertEqual(df.iloc[1]['precio'], 2000)



if __name__ == '__main__':
    unittest.main()
