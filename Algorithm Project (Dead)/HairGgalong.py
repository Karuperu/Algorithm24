import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

# 현재 스크립트의 디렉터리
script_dir = os.path.dirname(os.path.abspath(__file__))

# 파일의 경로
mainui = os.path.join(script_dir, "mainscreen.ui")
mainscreen = os.path.join(script_dir, "main.png")

# 파일 로드
form_class_main, base_class = uic.loadUiType(mainui)


class WindowClass(QMainWindow, form_class_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.B1_image()
        

    def loadImageFromFile(self):
        label_width = self.MainScreen.width()
        label_height = self.MainScreen.height()
        qPixmapFileVar = QPixmap(mainscreen)
        qPixmapFileVar = qPixmapFileVar.scaled(label_width, label_height)
        self.MainScreen.setPixmap(qPixmapFileVar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())