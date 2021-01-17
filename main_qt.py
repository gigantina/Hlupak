import sys
import sqlite3
import random
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from gases import start_gases
from realistic_gases import start_realistic_gases


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Главная")

        self.gases.setStyleSheet("background: transparent;")
        self.gases.setIcon(QIcon(f"data/images/gases.png"))
        self.gases.setIconSize(QSize(350, 350))
        self.gases.clicked.connect(self.start_gases)

        self.real_gases.setStyleSheet("background: transparent;")
        self.real_gases.setIcon(QIcon(f"data/images/real_gases.png"))
        self.real_gases.setIconSize(QSize(350, 350))
        self.real_gases.clicked.connect(self.start_real_gases)

    def start_gases(self):
        self.hide()
        start_gases()
        self.show()

    def start_real_gases(self):
        self.hide()
        start_realistic_gases()
        self.show()


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec())
