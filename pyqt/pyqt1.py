import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
# app = QtGui.QApplication(sys.argv)
# window=QtGui.QWidget()
# window.setGeometry()
# window.setWindowTitle("app")
# window.show()
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('hh.png'))
        self.show()
    def butt(self):
        btn=QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_app)
        btn.resize(btn.minimumSizeHunt())
        byn.move(0,0)
        self.show()
    def close_app(self):
        print("kkjfjb")
        sys.exit()
app =QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())