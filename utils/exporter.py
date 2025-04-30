#     Exporta los datos a un archivo Excel en la carpeta 'data',
#     agregando los nuevos datos al archivo existente si ya existe.
import pandas as pd
import os


def exportar_a_excel(data, archivo_salida="productos.xlsx"):
    """
    :parametro data: Lista de diccionarios con los datos de los productos.
    :parametro archivo_salida: Nombre del archivo Excel donde se guardarán los datos
    (por defecto 'productos.xlsx').
    """
    try:
        # Ruta de la carpeta 'data' en la raíz del proyecto
        ruta_data = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "data")

        if not os.path.exists(ruta_data):
            os.makedirs(ruta_data)  # Si la carpeta no existe, la crea

        # Ruta del archivo Excel
        archivo_completo = os.path.join(ruta_data, archivo_salida)

        # Si el archivo ya existe, cargamos los datos existentes
        if os.path.exists(archivo_completo):
            df_existente = pd.read_excel(archivo_completo, engine='openpyxl')
            # Convertimos los nuevos datos a un DataFrame
            df_nuevo = pd.DataFrame(data)
            # Concatenamos los datos existentes con los nuevos
            df = pd.concat([df_existente, df_nuevo], ignore_index=True)
        else:
            # Si el archivo no existe, simplemente creamos uno nuevo
            df = pd.DataFrame(data)

        # Exportamos el DataFrame al archivo Excel
        df.to_excel(archivo_completo, index=False, engine='openpyxl')

        print(f"Datos exportados exitosamente a {archivo_completo}")
    except Exception as e:
        print(f"Error al exportar los datos a Excel: {e}")
