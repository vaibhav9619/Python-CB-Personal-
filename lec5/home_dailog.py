from PyQt5 import QtWidgets,QtGui
from urllib import request
class HomeDialog(QtWidgets.QDialog):
    def __init__(self):
        super(HomeDialog, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        self.name = QtWidgets.QLabel("Helllo Coding blocks")
        self.name1 = QtWidgets.QLabel("My name is vaibhav")
        self.b = QtWidgets.QPushButton("Dont push me")
        self.g = QtWidgets.QLineEdit("helo mousii")
        self.h = QtWidgets.QDateEdit()
        j = QtWidgets.QDateTimeEdit()
        self.j1=QtWidgets.QLabel("Downloader")
        self.j2=QtWidgets.QLineEdit("")
        self.j3=QtWidgets.QPushButton("Click")

        self.b.clicked.connect(self.careless)
        self.g.textChanged.connect(self.edited)#provide refrence  without calling
        # connect is used to connect any function
        self.j3.clicked.connect(self.epic)

        layout.addWidget(self.name1)
        layout.addWidget(self.b)
        layout.addWidget(self.g)
        layout.addWidget(self.h)
        layout.addWidget(j)
        layout.addWidget(self.name)
        layout.addWidget(self.j1)
        layout.addWidget(self.j2)
        layout.addWidget(self.j3)
        self.setLayout(layout)
        # dia.show()
        # app.exec_()
    def careless(self):
        s1= self.g.text()
        self.name1.setText(s1)
        # print("Why are you so careless")
    def edited(self,text):
        self.name.setText(text)
        # print(text)
    # def epic(self,text1):
    #    d=QtGui.QPixmap(self.j2)
    #     ss=self.j2.text()
    #     self.


# pics map



