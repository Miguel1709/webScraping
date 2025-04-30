# styles.py
#archivo de Python que devuelve todo el codigo de QSS en forma de string
#el cual se lee desde el gui con self.setStyleSheet(get_stylesheet())

def get_stylesheet():
    return """
    QWidget {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
        stop:0 #ffffff, stop:1 #e0e0e0);
        font-family: "Segoe UI", "Arial";
        font-size: 14px;
        color: #333333;
    }

    QLabel {
        font-weight: bold;
        margin-top: 5px;
    }

    QLineEdit, QComboBox, QTextEdit {
        border: 1px solid #cccccc;
        border-radius: 8px;
        padding: 8px;
        background-color: #ffffff;
    }

    QPushButton {
        background-color: #3498db;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 10px;
    }

    QPushButton:hover {
        background-color: #2980b9;
    }

    QPushButton:pressed {
        background-color: #1c6690;
    }

    QTextEdit {
        background-color: #fafafa;
        border: 1px solid #ccc;
    }
    """
