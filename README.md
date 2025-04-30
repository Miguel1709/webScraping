
# 🕷️ Proyecto de Web Scraping con Selenium

Este proyecto es una solución completa de **web scraping automatizado** para extraer información de productos desde distintas plataformas de comercio electrónico como **Amazon, eBay, AliExpress, Mercado Libre y Shein**, utilizando **Python**, **Selenium** y módulos personalizados para el procesamiento y exportación de datos.

## 📌 Objetivo

Automatizar la recolección de datos clave (nombre y precio de productos) desde páginas dinámicas generadas con JavaScript, exportando los resultados a un archivo Excel y registrando cualquier error ocurrido durante el proceso.

## 🧠 Tecnologías utilizadas

- **Python 3.7+**
- **Selenium**: automatización del navegador.
- **pandas**: manipulación y exportación de datos.
- **openpyxl**: escritura de archivos Excel.
- **ChromeDriver**: controlador del navegador Chrome.
- **Logging personalizado** para gestión de errores.

## 📂 Estructura del proyecto

```
project_root/
│
├── scrapers/
│   ├── aliexpress_scraper.py
│   ├── ebay_scraper.py
│   ├── mercadolibre_scraper.py
│   └── ...                         # Más scrapers por plataforma
│
├── utils/
│   ├── logger.py                  # Manejo de errores (log)
│   ├── exporter.py                # Exportación a Excel
│   └── price_cleaner.py           # Limpieza de precios
│
├── productos_resultado.xlsx       # Archivo generado con los datos
└── README.md
```

## ⚙️ Requisitos

- Google Chrome instalado
- ChromeDriver descargado (compatible con tu versión de Chrome)
- Python 3.7 o superior

### 🧱 Instalación de dependencias

```bash
pip install selenium pandas openpyxl
```

## 🛠️ ¿Cómo funciona?

1. Cada scraper se enfoca en una tienda específica y extrae los productos usando selectores CSS o XPath según la estructura HTML.
2. Los precios se limpian y estandarizan con una función utilitaria.
3. Los productos se exportan a un archivo `.xlsx`, y los errores se guardan en un log.

## ▶️ Ejecución

Ejecuta el scraper de la tienda que desees, por ejemplo:

```bash
python scrapers/ebay_scraper.py
```

Puedes modificar la URL de búsqueda directamente en el archivo del scraper.

## 🧩 Modularidad

Este proyecto está dividido en módulos reutilizables:

- **logger.py**: registra errores durante el scraping.
- **exporter.py**: exporta los productos extraídos a un archivo Excel.
- **price_cleaner.py**: elimina símbolos, espacios y convierte los precios a formato numérico.

## 📋 Notas adicionales

- Los scrapers usan `--headless` para no mostrar el navegador.
- Algunas tiendas cambian constantemente su estructura HTML. Revisa los selectores si deja de funcionar.
- No está diseñado para extraer miles de productos. Es una herramienta de análisis y prueba educativa.
