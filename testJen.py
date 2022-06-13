import string
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import urllib.parse


#class Hotel:
 #   name: string

    #On recupere les donnees de l'hotel
    #@classmethod
    #def get_hotel_data(self, hotel_url):

#session = requests.session()
#headers = {'User-Agent': 'Mozilla/5.0'}

req = requests.get(url='https://www.unesco.org/fr/articles/sites-culturels-endommages-en-ukraine-confirmes-par-lunesco')
soup = BeautifulSoup(req.text, 'html.parser')
#data = soup.find_all("div",{"class":"field__item"})[0]
data = soup.find_all("ol")
#print(data)
liste = []
for row in data: 
    liste.append(row.get_text())
    #print(row.get_text())

print(liste)
len(liste)
print(liste[0])
#len(liste)
#df = pd.DataFrame( liste )
#print(df)

#liste = data.get_text().split('\n')   '''