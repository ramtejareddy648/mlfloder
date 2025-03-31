import requests
import csv
from bs4 import BeautifulSoup

url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")

image=soup.find_all("div",class_="PhYMAu")
print(image)
image1=[]

for i in image:
     j=i.img["src"]
   
     image1.append(j)
print(image1)


    

