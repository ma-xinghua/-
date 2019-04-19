import json
#这里由于要保存信息在各个类中使用，引入data类的实例Data，与json数据库同步
class data:
    def __init__(self):
        with open('file_list.json', 'r', encoding='utf-8') as f:  
            self.urllist = json.load(f)                         #self.urllist是存储着所有信息的字典
        self.name =''
        self.url =''
Data = data()