from bs4 import BeautifulSoup
import requests
import json
import tkinter
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

def create_soup(filename):      #获取与html文本一样的解析文档
        f = open(filename, encoding="utf-8")
        soup = BeautifulSoup(f, 'html.parser')
        return soup

def dumps_json(soup):   #将soup的内容写入字典
        openlist = dict()
        tag_a = soup.find_all('a')
        for a in tag_a:
                openlist[a.string] = a.get('href')
        merge(openlist) #调用函数，与原openlist合并

def merge(urllist2):
    with open('file_list.json', 'r', encoding='utf-8') as f_obj:
        urllist = json.load(f_obj)      #获取原oenlist的字典数据
    
    for name2,url2 in urllist2.items():
        find=1
        for name,url in urllist.items():        #寻找新字典中的数据是否在原字典中
            if (name==name2):
                x=url.split(';')        #以分号作为多地址的间隔
                if (url2 not in x):     
                    urllist[name]=urllist[name]+';'+url2
                find=0
                break
        if (find==1):
            urllist[name2]=url2    

    with open('file_list.json', 'w', encoding='utf-8') as f:
        json.dump(urllist, f, ensure_ascii=False, indent=2)     #写入json文件

def import1():  #导入的主函数
        root = tkinter.Tk()      
        root.withdraw()
        file = askopenfilename()        #询问选择哪个文件
        root.destroy()
        if (file!=""):  #若选择文件，就如上操作
                name = file.split('/')[-1]
                soup = create_soup(name)
                dumps_json(soup)
                return 1
        
        else:   #若没有选择文件，就不操作
                return 0



