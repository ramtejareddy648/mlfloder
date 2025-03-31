import threading
import requests
from bs4 import BeautifulSoup


def fetch(url):
    respone=requests.get(url)
    soup=BeautifulSoup(respone.content,"html.parser")
    print(f"fetch is {len(soup.text)}")

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]


threads=[]
for url in urls:
    thread=threading.Thread(target=fetch,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
