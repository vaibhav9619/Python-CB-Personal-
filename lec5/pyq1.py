from PyQt5 import  QtWidgets #pyqt is package adn Qtwidgets is module and we further work on classes
app = QtWidgets.QApplication([])#includes all the features dialog and window
dia = QtWidgets.QDialog()#shows dialog box
# there are windows and dialog box
# di = QtWidgets.QMainWindow()
layout=QtWidgets.QVBoxLayout() #vertical box to enter data vertically

#make object and add the functionality
name=QtWidgets.QLabel("Helllo Coding blocks")
name1=QtWidgets.QLabel("My name is vaibhav")
b=QtWidgets.QPushButton("Dont push me")
g=QtWidgets.QLineEdit("helo mousii")
h=QtWidgets.QDateEdit()
j=QtWidgets.QDateTimeEdit()

# store that in layout for display
layout.addWidget(name1)
layout.addWidget(b)
layout.addWidget(g)
layout.addWidget(h)
layout.addWidget(j)
layout.addWidget(name) #name is set to layout
dia.setLayout(layout)#layout is further set to dialog
#show the dialog it will display the name string
dia.show()
# di.show()
app.exec_()


