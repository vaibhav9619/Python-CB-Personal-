from PyQt5 import QtWidgets
import home_dailog
class Parent_dai(QtWidgets.QDialog):
    def __init__(self):
        super(Parent_dai, self).__init__()
        layout1=QtWidgets.QVBoxLayout()
        home=home_dailog.HomeDialog()
        home1=home_dailog.HomeDialog()
        layout1.addWidget(home)
        layout1.addWidget(home1)
        self.setLayout(layout1)


