import json
class data:
    def __init__(self):
        with open('file_list.json', 'r', encoding='utf-8') as f:  #初始化界面，打印所有项目名称
            self.urllist = json.load(f)                         #self.urllist是存储着所有信息的字典
        self.name =''
        self.url =''

Data = data()