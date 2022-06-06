# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:26:10 2022

@author: PIERO
"""


import os

def crear(nombre,contenido):
    archivo= open(nombre,"w")
    archivo.write(contenido)
    archivo.close()
    
    
def eliminar(nombre):
    os.remove(nombre)

def agregar(nombre,contenido):
    archivo=open(nombre,"at")
    archivo.write(contenido)
    archivo.close()
def ver(nombre):
    archivo=open(nombre,"rt")
    contenido=archivo.read()
    return contenido
    