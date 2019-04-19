#coding=utf-8
import sys
import json
import webbrowser
from data import *
from down_mark import *
from main_interface import Ui_Dialog
from add_interface import Ui_Dialog_add
from PyQt5 import QtWidgets, QtGui
from pypinyin import Style
import pypinyin

class add_window(QtWidgets.QWidget, Ui_Dialog_add):
    def __init__(self,prior):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.prior=prior          #传入父窗口

    def confirm(self):           #添加功能的实现
        Data.name=self.lineEdit.text()
        Data.url=self.lineEdit_2.text()
        for i in Data.urllist:       #处理已有关键词的情况
            if(Data.name==i):
                Data.urllist[i]=Data.urllist[i]+';'+Data.url      
                with open('file_list.json', 'w', encoding='utf-8') as f:
                    json.dump(Data.urllist, f, ensure_ascii=False, indent=2)
                f.close()
                self.hide()      #隐藏窗口而不是关闭窗口   
                self.lineEdit.clear()
                self.lineEdit_2.clear()      
                return
        Data.urllist.update({Data.name:Data.url})    #处理没有关键词的情况
        with open('file_list.json', 'w', encoding='utf-8') as f:
            json.dump(Data.urllist, f, ensure_ascii=False, indent=2)
        f.close()
        self.prior.adddisplay()
        self.hide()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def cancel(self):   #取消添加
        self.hide()
        self.lineEdit.clear()
        self.lineEdit_2.clear()


class father_window(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):                           #构造函数
        super(father_window, self).__init__()
        self.setupUi(self)
        for name in Data.urllist:
            self.listWidget.addItem(name)                    
        self.listWidget.doubleClicked.connect(self.open)
        self.lineEdit.textChanged.connect(self.showlist)    #检测父窗口中输入框的文字是否变化，并发射信号，连接showlist函数
        self.add_app = QtWidgets.QApplication(sys.argv)
        self.add_show = add_window(self)

    def add(self):
        self.add_show.show()    #显示子窗口
                                         
    def delete(self):            #删除功能的实现
        deletename=self.listWidget.currentItem().text()
        self.listWidget.takeItem(self.listWidget.currentRow())   #删除选中的一行
        Data.urllist.pop(deletename)                             #字典中进行更新 
        with open('file_list.json', 'w', encoding='utf-8') as f:    #json数据库更新
                    json.dump(Data.urllist, f, ensure_ascii=False, indent=2)
        f.close()


    def import_list(self):
        t=import1(self)
        if (t==1):
            information=QMessageBox.information(self,"提示","成功")
        elif (t==0):
            information=QMessageBox.information(self,"提示","没有文件导入")
            
    def open(self):               #双击打开功能的实现
        name=self.listWidget.currentItem().text()
        urllong=Data.urllist[name]
        url=urllong.split(';')      #使用；分隔地址，全部打开
        for thing in url:
            webbrowser.open(thing)

    def adddisplay(self):              #在添加完成后显示内容
        self.listWidget.addItem(Data.name) 

    def showlist(self): #用于搜索后结果的显示
        keywd = self.lineEdit.text().strip()
        if keywd:
            self.listWidget.clear() #清空显示框
            for item in Data.urllist:   #对大小写及拼音的识别转换
                if (keywd.lower() in item.lower()) or (keywd.lower() in pypinyin.slug(item.lower(), separator='') or
                                                       (keywd.lower() in pypinyin.slug(item.lower(),
                                                                                       style=Style.FIRST_LETTER,
                                                                                       separator=''))):
                    self.listWidget.addItem(item)  # 加载搜索结果
        else:
            self.listWidget.clear()
            for item in Data.urllist:
                self.listWidget.addItem(item)  # 空字符时，加载所有列表

if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myshow = father_window()
    myshow.show()
    sys.exit(app.exec_())
    
