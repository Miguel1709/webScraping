from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log_error
from utils.exporter import exportar_a_excel
import time


def obtener_productos_amazon(url):
    opciones = Options()
    opciones.add_argument("--headless")
    opciones.add_argument("--disable-gpu")
    servicio = Service(executable_path="C:\\chromeDriver\\chromedriver.exe")

    driver = webdriver.Chrome(service=servicio, options=opciones)
    productos = []

    try:
        driver.get(url)

        # Espera extendida para carga completa
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-main-slot .s-result-item"))
        )

        time.sleep(5)  # Tiempo adicional para asegurarse de que cargue todo

        contenedores = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
        print(f"Contenedores encontrados: {len(contenedores)}")

        for contenedor in contenedores:
            try:
                nombre = contenedor.find_element(By.CSS_SELECTOR, ".a-text-normal").text

                try:
                    precio_entero = contenedor.find_element(By.CSS_SELECTOR, ".a-price .a-price-whole").text
                    precio_decimal = contenedor.find_element(By.CSS_SELECTOR, ".a-price .a-price-fraction").text
                    precio = f"${precio_entero},{precio_decimal}"
                except Exception:
                    precio = "No disponible"

                productos.append({'nombre': nombre, 'precio': precio})
                time.sleep(1)

            except Exception as e:
                error_message = f"Error al extraer producto: {e}"
                print(error_message)
                log_error(error_message)

        driver.quit()

    except Exception as e:
        error_message = f"Error general en Amazon scraper: {e}"
        print(error_message)
        log_error(error_message)
        driver.quit()

    print(f"Total productos encontrados: {len(productos)}")

    # Exportar los productos a un archivo Excel usando el módulo exporter
    exportar_a_excel(productos, "productos_amazon.xlsx")

    return productos
