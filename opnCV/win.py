
from PyQt5 import QtWidgets
from detect1 import ko

app=QtWidgets.QApplication([])

dia=QtWidgets.QDialog()
dia.setWindowTitle("Capture")
layout=QtWidgets.QVBoxLayout()
name=QtWidgets.QPushButton("Click to Capture")

name.clicked.connect(ko)
# name.addAction()
layout.addWidget(name)
dia.setLayout(layout)
# dia.showFullScreen()
dia.show()
app.exec_()