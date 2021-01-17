import sys
import sqlite3
import random
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from gases import start_gases
from realistic_gases import start_realistic_gases
from lever import start_lever
from magnet import start_magnet
from comvessels import start_vessel


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Главная")

        font = 17
        self.gases.setStyleSheet(f"background: transparent;")
        self.gases.setIcon(QIcon(f"data/images/gases.png"))
        self.gases.setIconSize(QSize(350, 350))
        self.gases.clicked.connect(self.start_gases)

        self.real_gases.setStyleSheet(f"background: transparent;")
        self.real_gases.setIcon(QIcon(f"data/images/real_gases.png"))
        self.real_gases.setIconSize(QSize(350, 350))
        self.real_gases.clicked.connect(self.start_real_gases)

        self.lever.setStyleSheet(f"background: transparent;")
        self.lever.setIcon(QIcon(f"data/images/lever.png"))
        self.lever.setIconSize(QSize(350, 350))
        self.lever.clicked.connect(self.start_lever)

        self.magnet.setStyleSheet(f"background: transparent;")
        self.magnet.setIcon(QIcon(f"data/images/magnets.png"))
        self.magnet.setIconSize(QSize(350, 350))
        self.magnet.clicked.connect(self.start_magnets)

        self.vessels.setStyleSheet(f"background: transparent;")
        self.vessels.setIcon(QIcon(f"data/images/vessel.png"))
        self.vessels.setIconSize(QSize(350, 350))
        self.vessels.clicked.connect(self.start_vessels)
    def start_vessels(self):
        self.hide()
        start_vessel()
        self.show()


    def start_gases(self):
        self.hide()
        start_gases()
        self.show()

    def start_real_gases(self):
        self.hide()
        start_realistic_gases()
        self.show()

    def start_lever(self):
        self.hide()
        start_lever()
        self.show()

    def start_magnets(self):
        self.hide()
        start_magnet()
        self.show()


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec())
