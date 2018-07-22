from PyQt5 import QtWidgets
import parent_dialog #home_dialog is a module which contain different class ie homedailog()
app=QtWidgets.QApplication([])
home=parent_dialog.Parent_dai()
home.show()
exit(app.exec_())