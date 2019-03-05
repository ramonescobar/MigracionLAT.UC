import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import app

def get_data_pais(c):
    base_url = 'http://www.google.com/search?q={}&btnI'
    terminos_a_buscar = ['https://datosmacro.expansion.com/demografia/migracion/inmigracion/', c]
    url = base_url.format('+'.join(terminos_a_buscar))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all(class_="table tabledat table-striped table-condensed table-hover")
    print(content)
    content = content.pop(1)
    content2 = content.findAll("td", { "class" : "numero"})
    content1 = content.findAll("td", { "class" : None})
    agregado1 = []
    for num in range(len(content1)):
        agregado1.append(content1[num].text)
    agregado2 = []
    for num in range(len(content2)):
        agregado2.append(content2[num].text)
    d = {'País de entrada': c,'Países de salida': agregado1, 'Número de personas': agregado2}
    df1 = pd.DataFrame(data=d)
    return df1

lista=app.lista

dftotal = pd.DataFrame()
df1 = pd.DataFrame()
for c in lista:
    dftotal = pd.concat([dftotal,get_data_pais(c)])
    print(dftotal)
dftotal.set_index('País de entrada', inplace=True)
dftotal.to_csv("MXP.csv", sep='\t', encoding='utf-8')
