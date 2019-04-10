import sys
from main_interface import Ui_Dialog
from PyQt5 import QtWidgets, QtGui

class father_window(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(father_window, self).__init__()
        self.setupUi(self)

    def add(self):
        print ("add")

    def delete(self):
        print ("delete")

    def import_list(self):
        print ("import")


if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myshow = father_window()
    myshow.show()
    sys.exit(app.exec_())
    
