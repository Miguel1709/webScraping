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
import time

def obtener_productos_aliexpress(url):
    opciones = Options()
    opciones.add_argument("--headless")
    opciones.add_argument("--disable-gpu")
    servicio = Service(executable_path="C:\\chromeDriver\\chromedriver.exe")

    driver = webdriver.Chrome(service=servicio, options=opciones)
    productos = []

    try:
        driver.get(url)
        time.sleep(10)

        # Esperamos que cargue algún contenedor de producto
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.lj_j4"))
        )

        # Hacemos scroll para cargar más productos
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        contenedores = driver.find_elements(By.CSS_SELECTOR, "div.lj_j4")
        print(f"Contenedores encontrados: {len(contenedores)}")

        for contenedor in contenedores:
            try:
                nombre = contenedor.find_element(By.CSS_SELECTOR, "h3.lj_kp").text.strip()
                try:
                    # Buscamos el contenedor de precio que esté justo después
                    contenedor_precio = contenedor.find_element(By.XPATH, ".//following::div[contains(@class,'lj_cr')][1]//div[contains(@class,'lj_kr')]")
                    spans = contenedor_precio.find_elements(By.TAG_NAME, "span")
                    precio_base = ''.join([span.text.strip() for span in spans])
                    precio = limpiar_precio(precio_base)
                except NoSuchElementException:
                    precio = "No disponible"

                productos.append({'nombre': nombre, 'precio': precio})
                time.sleep(1)
            except Exception as e:
                log_error(f"Error al extraer producto: {e}")

        driver.quit()

    except Exception as e:
        log_error(f"Error general en AliExpress scraper: {e}")
        driver.quit()

    print(f"Total productos encontrados: {len(productos)}")

    # Exportar los productos a un archivo Excel usando el módulo exporter
    exportar_a_excel(productos, "productos_aliexpress.xlsx")

    return productos
