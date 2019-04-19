from bs4 import BeautifulSoup
import requests
import json
from tkinter import Tk
from data import *
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

def create_soup(filename):
        f = open(filename, encoding="utf-8")
        soup = BeautifulSoup(f, 'html.parser')
        return soup


def dumps_json(soup,father_window):
        openlist = dict()
        tag_a = soup.find_all('a')
        for a in tag_a:
                openlist[a.string] = a.get('href')
        merge(openlist,father_window)

def merge(urllist2,father_window):
    with open('file_list.json', 'r', encoding='utf-8') as f_obj:
        urllist = json.load(f_obj)
    
    for name2,url2 in urllist2.items():
        find=1
        for name,url in urllist.items():
            if (name==name2):
                x=url.split(';')
                if (url2 not in x):
                    urllist[name]=urllist[name]+';'+url2
                    Data.urllist[name]=Data.urllist[name]+';'+url2 #更新数据
                find=0
                break
        if (find==1):
            urllist[name2]=url2    
            Data.urllist.update({name2:url2})    #将导入的信息显示在屏幕上
            father_window.listWidget.addItem(name2)
       
    #for name,url in urllist.items():
    #   print (name,url)


    with open('file_list.json', 'w', encoding='utf-8') as f:
        json.dump(urllist, f, ensure_ascii=False, indent=2)

def import1(father_window):
        root = tkinter.Tk()      
        root.withdraw()
        file = askopenfilename()
        root.destroy()
        if (file!=""):
                name = file.split('/')[-1]
                soup = create_soup(name)
                dumps_json(soup,father_window)
                return 1      
        else:
                return 0



