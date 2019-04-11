from bs4 import BeautifulSoup
import requests
import json

def create_soup():
        f = open("Microsoft_Edge_‎04_‎11_‎2019.html", encoding="utf-8")
        soup = BeautifulSoup(f, 'html.parser')
        return soup


def dumps_json(soup):
        openlist = dict()
        tag_a = soup.find_all('a')
        for a in tag_a:
                openlist[a.string] = a.get('href')
        merge(openlist)

def merge(urllist2):
    with open('file_list.json', 'r', encoding='utf-8') as f_obj:
        urllist = json.load(f_obj)
    
    for name2,url2 in urllist2.items():
        find=1
        for name,url in urllist.items():
            if (name==name2):
                x=url.split(';')
                if (url2 not in x):
                    urllist[name]=urllist[name]+';'+url2
                find=0
                break
        if (find==1):
            urllist[name2]=url2
       
    #for name,url in urllist.items():
    #   print (name,url)


    with open('file_list.json', 'w', encoding='utf-8') as f:
        json.dump(urllist, f, ensure_ascii=False, indent=2)

def main():
        soup = create_soup()
        dumps_json(soup)
                

if __name__ == '__main__':
        main()


