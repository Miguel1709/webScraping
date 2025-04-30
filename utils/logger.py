#archivo log para el manejo de errores

import os
from datetime import datetime

#dirección del archivo
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
#nombre del archivo
LOG_FILE = os.path.join(LOG_DIR, 'errores.log')

#crea el directorio de logs si no existe
os.makedirs(LOG_DIR, exist_ok=True)

#guarda errores de lectura de campos durante el scraping con la fecha
def log_error(mensaje):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {mensaje}\n")
