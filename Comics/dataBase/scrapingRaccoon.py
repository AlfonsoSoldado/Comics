'''
Created on 10 ene. 2018

@author: alfon
'''

from bs4 import BeautifulSoup
from pip._vendor import requests

enlace = "http://www.raccoongames.es/es/productos/comics/"

dirindex = "Index"

cont = 0
todo = []

def obtenerDatos(enlace, cont):
    req = requests.get(enlace)
    data = req.text
    print(enlace)
    soup = BeautifulSoup(data, 'html.parser')
    temas = soup.find_all("div", attrs={"class":"ctr-titulo-precio"})
    imagenes = soup.find_all("div", attrs={"class":"producto-lst"})
    
    for tema, imagen in zip(temas, imagenes):
        
        todos_datos = []
        titulo = tema.find('a').get_text()
        precio = tema.find('span', attrs={'class':'precio-actual'}).get_text()[2:]
        enlace = 'http://www.raccoongames.es' + tema.find('a')['href']
        imagen = 'http://www.raccoongames.es' + imagen.find('img')['src']
        
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
            enlaceSiguiente = "http://www.raccoongames.es/es/productos/comics/" + str(sum)
            obtenerDatos(enlaceSiguiente, cont)
    
    return todo