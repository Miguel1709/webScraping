#importar funciones (módulos)
from scraper import obtener_productos_amazon, obtener_productos_ebay, obtener_productos_aliexpress, obtener_productos_mercadolibre

#se configura la función que se llamará dependiendo del sitio elegido
def obtener_productos(url, site):
    if site == "amazon":
        return obtener_productos_amazon(url)
    elif site == "ebay":
        return obtener_productos_ebay(url)
    elif site == "aliexpress":
        return obtener_productos_aliexpress(url)
    elif site == "mercadoLibre":
        return obtener_productos_mercadolibre(url)
    else:
        raise ValueError("Sitio no soportado")

if __name__ == "__main__": #si se ejecuta el main, se hace una prueba desde la consola
    url = input("Ingrese la URL: ")
    site = input("Ingrese el nombre del sitio (amazon, ebay, aliexpress, mercadoLibre): ")

    productos = obtener_productos(url, site)
    for producto in productos:
        print(producto)
