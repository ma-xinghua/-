#coding=utf-8
import sys
from down_mark import*
from main_interface import Ui_Dialog
from add_interface import Ui_Dialog_add
from PyQt5 import QtWidgets, QtGui

class add_window(QtWidgets.QWidget, Ui_Dialog_add):
    def __init__(self):
        super(add_window, self).__init__()
        self.setupUi(self)

    def confirm(self):
        print ("confirm")

    def cancel(self):
        print ("cancel")


class father_window(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(father_window, self).__init__()
        self.setupUi(self)

    def add(self):
        self.add_app = QtWidgets.QApplication(sys.argv)
        self.add_show = add_window()
        self.add_show.show()

    def delete(self):
        print ("delete")

    def import_list(self):
        import1()
        information=QMessageBox.information(self,"提示","成功")
        


if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myshow = father_window()
    myshow.show()
    sys.exit(app.exec_())
    
