# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:38:36 2022

@author: PIERO
"""

import prueba

def menu():
    print("1.crear")
    print("2.agregar")
    print("3.eliminar")
    print("4.ver")
    


while True:
    menu()
    op=int(input("Digite opcion: "))
    
    if op==1:
        nombre=input("Digite nombre: ")
        contenido=input("Digite contenido: ")
        prueba.crear(nombre, contenido)
    elif op==2:
        nombre=input("Digite nombre: ")
        contenido=input("Digite contenido: ")
        prueba.agregar(nombre, contenido)
    elif op==3:
        nombre=input("Digite nombre: ")
        prueba.eliminar(nombre)
    elif op==4:
        nombre=input("Digite nombre: ")
        print(prueba.ver(nombre))
    else:
        break