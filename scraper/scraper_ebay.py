from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log_error
from utils.exporter import exportar_a_excel
from utils.price_cleaner import limpiar_precio


def obtener_productos_ebay(url):
    opciones = Options()
    opciones.add_argument('--headless')
    opciones.add_argument('--disable-gpu')
    servicio = Service(executable_path="C:\\chromeDriver\\chromedriver.exe")

    driver = webdriver.Chrome(service=servicio, options=opciones)
    productos = []

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "s-item"))
        )

        contenedores = driver.find_elements(By.CLASS_NAME, "s-item")
        print(f"Contenedores encontrados: {len(contenedores)}")

        for contenedor in contenedores:
            try:
                nombre = contenedor.find_element(By.CSS_SELECTOR, "div.s-item__title span").text
                precio_base = contenedor.find_element(By.CSS_SELECTOR, "span.s-item__price").text
                precio = limpiar_precio(precio_base)
                productos.append({'nombre': nombre, 'precio': precio})
            except Exception as e:
                print(f"Error al extraer producto: {e}")
                log_error(str(e))
                continue

    except Exception as e:
        print(f"Error general en eBay scraper: {e}")
        log_error(str(e))

    driver.quit()
    print(f"Total productos encontrados: {len(productos)}")

    # Exportar los productos a un archivo Excel usando el módulo exporter
    exportar_a_excel(productos, "productos_ebay.xlsx")

    return productos
