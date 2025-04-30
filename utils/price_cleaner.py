import re

def limpiar_precio(precio_raw):
    if not precio_raw:
        return None

    # Eliminar saltos de línea y espacios múltiples
    precio_raw = precio_raw.replace('\n', ' ').replace('\r', ' ')
    precio_raw = re.sub(r'\s+', ' ', precio_raw).strip()

    # Eliminar cualquier cosa relacionada con descuentos como "15% OFF"
    precio_raw = re.sub(r'\d{1,3}% OFF', '', precio_raw, flags=re.IGNORECASE)


    # Eliminar todo lo que no sea número, punto, coma, espacio o 'a'
    precio_limpio = re.sub(r'[^\d.,\sa]', '', precio_raw)

    # Si hay un rango (como "100 a 200"), quedarse con el segundo número
    if ' a ' in precio_limpio:
        precio_limpio = precio_limpio.split(' a ')[-1]

    # Eliminar espacios entre miles
    precio_limpio = precio_limpio.replace(' ', '')

    # Reglas de puntos y comas
    if precio_limpio.count('.') > 1 and precio_limpio.count(',') == 0:
        precio_limpio = precio_limpio.replace('.', '')
    elif precio_limpio.count(',') == 1 and precio_limpio.count('.') == 0:
        precio_limpio = precio_limpio.replace(',', '.')
    elif precio_limpio.count('.') > 0 and precio_limpio.count(',') > 0:
        precio_limpio = precio_limpio.replace('.', '')
        precio_limpio = precio_limpio.replace(',', '.')

    try:
        return float(precio_limpio)
    except ValueError:
        return None
