#convierte la carpeta "scraper" en un paquete de Python para que los archivos puedan
#ser exportados como módulos desde otras partes del proyecto y así utilizar sus funciones
from .scraper_amazon import obtener_productos_amazon
from .scraper_ebay import obtener_productos_ebay
from .scraper_aliexpress import obtener_productos_aliexpress
from .scraper_mercadoLibre import obtener_productos_mercadolibre
