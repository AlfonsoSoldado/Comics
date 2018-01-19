'''
Created on 10 ene. 2018

@author: alfon
'''

from bs4 import BeautifulSoup
from pip._vendor import requests

dirindex = "Index"

cont = 0
todo = []

def obtenerDatos(enlace, cont):
    req = requests.get(enlace, verify=False)
    data = req.text
    print(enlace)
    soup = BeautifulSoup(data, 'html.parser')
    temas = soup.find_all("li", attrs={"class":"item"})
    
    for tema in temas:
            
        todos_datos = []
        titulo = tema.find('h3', attrs={'class':'product-name single-line-name'}).get_text().strip()
        preci = tema.find('p', attrs={'class':'special-price'})
        enlace = tema.find('a')['href']
        imagen = tema.find('a').find('img')['src']
        
        precio = preci.getText().split()[2]
        
        todos_datos.append(titulo)
        todos_datos.append(precio)
        todos_datos.append(enlace)
        todos_datos.append(imagen)
        
        todo.append(todos_datos)
        
        cont = cont + 1
        
    sum = 1  # @ReservedAssignment
    
    if (cont % 12 == 0):
            sum = cont / 12  # @ReservedAssignment
            sum = sum + 1  # @ReservedAssignment
            print(sum)
            enlaceSiguiente = "https://www.normacomics.com/amlanding/page/view/page_id/200/am_landing/comic-americano/?p=" + str(sum)
            obtenerDatos(enlaceSiguiente, cont)
    
    return todo