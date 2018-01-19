'''
Created on 10 ene. 2018

@author: alfon
'''

from Tkinter import *  # @UnusedWildImport
from __builtin__ import str
import sqlite3
import tkMessageBox

import scrapingRaccoon
import scrapingNormaComics


enlaceRaccoon = "http://www.raccoongames.es/es/productos/comics/"
enlaceNorma = "https://www.normacomics.com/amlanding/page/view/page_id/200/am_landing/comic-americano/?p=1"
cont = 0
todo = []

def almacenar_bd():
    conn = sqlite3.connect('comics.db')
    conn.text_factory = str  # para evitar problemas con el conjunto de caracteres que maneja la BD
    conn.execute("DROP TABLE IF EXISTS COMICS")   
    conn.execute('''CREATE TABLE COMICS
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       NOMBRE TEXT NOT NULL,
       PRECIO INTEGER NOT NULL,
       ENLACE TEXT NOT NULL,
       IMAGEN TEXT NOT NULL);''')
    
    lRaccoon = scrapingRaccoon.obtenerDatos(enlaceRaccoon, cont)
    lNorma = scrapingNormaComics.obtenerDatos(enlaceNorma, cont)
    
    for i in lRaccoon:
        todo.append(i)
    for e in lNorma:
        todo.append(e)
    print(todo)

    for i in todo:
        print i
        conn.execute("INSERT INTO COMICS (NOMBRE,PRECIO,ENLACE,IMAGEN) VALUES (?,?,?,?)",(i[0],i[1],i[2],i[3]))
    conn.commit()
    cursor = conn.execute("SELECT COUNT(*) FROM COMICS")
    tkMessageBox.showinfo( "Base Datos", "Base de datos creada correctamente \nHay " + str(cursor.fetchone()[0]) + " registros")
    conn.close()
    
def listar_bd():
    conn = sqlite3.connect('comics.db')
    conn.text_factory = str  
    cursor = conn.execute("SELECT NOMBRE,PRECIO,ENLACE,IMAGEN FROM COMICS")
    imprimir_etiqueta(cursor)
    conn.close()
    
def imprimir_etiqueta(cursor):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    for row in cursor:
        lb.insert(END,row[0])
        lb.insert(END,row[1])
        lb.insert(END,row[2])
        lb.insert(END,row[3])
        lb.insert(END,'')
    lb.pack(side = LEFT, fill = BOTH)
    sc.config(command = lb.yview)
    
def buscar_nombre():
    def listar_busqueda(event):
        conn = sqlite3.connect('comics.db')
        conn.text_factory = str
        s = "%"+en.get()+"%"
        cursor = conn.execute("""SELECT NOMBRE, PRECIO, ENLACE, IMAGEN FROM COMICS WHERE NOMBRE LIKE (?)""", (s,))
        imprimir_etiqueta(cursor)
        conn.close()
    v = Toplevel()
    lb = Label(v, text="Introduzca el nombre del comic que esta buscando: ")
    lb.pack(side=LEFT)
    en = Entry(v)
    en.bind("<Return>", listar_busqueda)
    en.pack(side=LEFT)
    
def ventana():
    root = Tk()
    menubar = Menu(root)
    datosmenu = Menu(menubar, tearoff=0)
    datosmenu.add_command(label="Cargar", command=almacenar_bd)
    datosmenu.add_command(label="Mostrar", command=listar_bd)
    datosmenu.add_command(label="Salir", command=root.quit)
     
    menubar.add_cascade(label="Datos", menu=datosmenu)
     
    buscarmenu = Menu(menubar, tearoff=0)
    buscarmenu.add_command(label="Buscar comic", command=buscar_nombre)
#     buscarmenu.add_command(label="Autor", command=buscar_autor)
#     buscarmenu.add_command(label="Fecha", command=donothing)
     
    menubar.add_cascade(label="Buscar", menu=buscarmenu)
     
#     estadisticasmenu = Menu(menubar, tearoff=0)
#     estadisticasmenu.add_command(label="Noticias mas valoradas", command=donothing)
#     estadisticasmenu.add_command(label="Autores mas activos", command=donothing)
#     menubar.add_cascade(label="Estadisticas", menu=estadisticasmenu)
     
    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    ventana()