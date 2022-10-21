from cgitb import text
import requests
from bs4 import BeautifulSoup

class Transaction:
    def __init__(self, url):
        self.url = url
        self.user_agent = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
        self.response = requests.get(url = self.url, headers= self.user_agent).text
        self.soup = BeautifulSoup(self.response , 'lxml')
 
    def get(self):
        Txnid = self.soup.find_all('span' , {'class' : "hash-tag text-truncate"})
        file = open("sample.txt", 'w')
        file.write("transaction Hash :")
        file.write("\n")
        count = 1
        for i in Txnid:
            file.write(f'{count}.{i.text.strip()}')
            file.write("\n")
            count+=1
        file.close()
         
dev1 = Transaction(url = 'https://bscscan.com/txs')
print(dev1.get())

