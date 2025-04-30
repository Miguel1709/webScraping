import unittest
import os
from datetime import datetime
from utils.logger import log_error, LOG_FILE


class TestLogger(unittest.TestCase):

    def test_log_error(self):
        #mensaje de prueba único
        mensaje_prueba = f"Mensaje de prueba {datetime.now().strftime('%H%M%S')}"

        #función a testear
        log_error(mensaje_prueba)

        #verificamos que el archivo existe
        self.assertTrue(os.path.exists(LOG_FILE), "El archivo de log no fue creado.")

        #se lee el contenido del archivo para buscar el mensaje
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            contenido = f.read()

        #verificamos que nuestro mensaje esté en el contenido
        self.assertIn(mensaje_prueba, contenido, "El mensaje no se encontró en el archivo de log.")


if __name__ == '__main__':
    unittest.main()
