from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI!")
        self.setGeometry(100, 100, 2000, 1000)
        self.setWindowIcon(QIcon("search.png"))

        label = QLabel(self)
        label.setText("Hello World!")
        label.setFont(QFont("Arial", 40))
        label.setGeometry(600, 450, 700, 150)
        label.setStyleSheet("color: red;"
                            "background-color: black;"
                            "border: 2px solid green;"
                            "border-radius: 10px;"
                            "padding: 10px;")
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()