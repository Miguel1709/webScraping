# app_ui.py
#importar librerías de PySide, styles y módulos
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, \
    QComboBox, QTextEdit
from scraper import obtener_productos_amazon, obtener_productos_ebay, obtener_productos_aliexpress, obtener_productos_mercadolibre
from gui.styles import get_stylesheet
import sys
import os
#especificar ruta para buscar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'webScraping/')))


class AppWindow(QWidget): #se crea una subclase de QWidget para personalizarla
    def __init__(self): #iniciar el AppWindow
        super().__init__() #constructor de la clase base QWidget para que se ejecute correctamente

        self.setWindowTitle("Web Scraping Productos")
        self.setGeometry(100, 100, 700, 500)

        self.init_ui() #mostrar la ventana personalizada que se definió
        self.setStyleSheet(get_stylesheet()) #función para utilizar los estilos definidos

    def init_ui(self):
        # Layouts
        main_layout = QVBoxLayout()

        # URL input
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Ingrese la URL del producto")

        # Sitio selector
        self.site_selector = QComboBox(self)
        self.site_selector.addItems(["amazon", "ebay", "aliexpress", "mercadoLibre"])

        # Botón de obtener productos
        self.scrape_button = QPushButton("Obtener productos", self)
        self.scrape_button.clicked.connect(self.on_scrape_button_clicked)

        # Area para mostrar los resultados
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)

        # Add widgets to layout
        main_layout.addWidget(QLabel("URL del producto:"))
        main_layout.addWidget(self.url_input)
        main_layout.addWidget(QLabel("Selecciona el sitio:"))
        main_layout.addWidget(self.site_selector)
        main_layout.addWidget(self.scrape_button)
        main_layout.addWidget(QLabel("Resultados:"))
        main_layout.addWidget(self.result_text)

        self.setLayout(main_layout)

    def on_scrape_button_clicked(self):
        #tomar texto de los inputs
        url = self.url_input.text()
        site = self.site_selector.currentText()

        if url: #validar elección y url
            try:
                if site == "amazon":
                    productos = obtener_productos_amazon(url)
                elif site == "ebay":
                    productos = obtener_productos_ebay(url)
                elif site == "aliexpress":
                    productos = obtener_productos_aliexpress(url)
                elif site == "mercadoLibre":
                    productos = obtener_productos_mercadolibre(url)

                if productos:
                    self.result_text.clear() #se limpia el layout de resultados
                    for producto in productos:
                        self.result_text.append(f"Nombre: {producto['nombre']}")
                        self.result_text.append(f"Precio: {producto['precio']}")
                        self.result_text.append("-" * 40)
                else:
                    self.result_text.setText("No se encontraron productos.")
            except Exception as e:
                self.result_text.setText(f"Error al obtener los productos: {str(e)}")
        else:
            self.result_text.setText("Por favor, ingrese una URL.")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv) #inicia la aplicación gráfica
    window = AppWindow() #crea una instancia de la ventana definida
    window.show() #muestra la ventana
    sys.exit(app.exec()) #se corre la ventana hasta que el usuario la cierre
