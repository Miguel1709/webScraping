from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log_error
from utils.exporter import exportar_a_excel
from utils.price_cleaner import limpiar_precio
from selenium.common.exceptions import NoSuchElementException


def obtener_productos_mercadolibre(url):
    opciones = Options()
    opciones.add_argument('--headless')
    opciones.add_argument('--disable-gpu')
    servicio = Service(executable_path="C:\\chromeDriver\\chromedriver.exe")

    driver = webdriver.Chrome(service=servicio, options=opciones)
    productos = []

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "ui-search-layout__item"))
        )

        contenedores = driver.find_elements(By.CLASS_NAME, "ui-search-layout__item")
        print(f"Contenedores encontrados: {len(contenedores)}")

        for i in range(len(contenedores)):
            try:
                # Re-obtenemos el contenedor en cada iteración
                contenedor = driver.find_elements(By.CLASS_NAME, "ui-search-layout__item")[i]

                # Obtener el nombre del producto
                nombre = contenedor.find_element(By.CLASS_NAME, "poly-component__title").text

                # Intentar obtener el precio con descuento (si existe)
                try:
                    precio_base = contenedor.find_element(By.CLASS_NAME, "poly-price__current").text
                    precio = limpiar_precio(precio_base)
                except NoSuchElementException:
                    # Si no tiene descuento, tomar el precio normal
                    precio_base = contenedor.find_element(By.CLASS_NAME, "poly-component__price").text
                    precio = limpiar_precio(precio_base)


                productos.append({'nombre': nombre, 'precio': precio})

            except Exception as e:
                print(f"Error al extraer producto: {e}")
                log_error(str(e))
                continue


    except Exception as e:
        print(f"Error general en Mercado Libre scraper: {e}")
        log_error(str(e))

    driver.quit()
    print(f"Total productos encontrados: {len(productos)}")

    # Exportar los productos a un archivo Excel usando el módulo exporter
    exportar_a_excel(productos, "productos_mercadoLibre.xlsx")

    return productos
