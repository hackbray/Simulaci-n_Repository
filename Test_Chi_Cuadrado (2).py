# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:36:38 2015

@author: ESTUDIANTE
"""

import numpy as np
import math


def randuX(n):
    """Retorna una lista que contiene n valores aproximados a una distribución uniforme U(0,1).
    
    Esto a partir de un GENERADOR CONGRUENCIAL MIXTO... Xn = (170*Xn-1 + 1) mod 30323.
    """
    x0 = 7          #Este es el valor semilla elegido.
    valores = []
    for i in range(0,n):
        xi = (170*x0 + 1)%30323
        ui = xi/30323.0
        valores.append(ui)
        x0 = xi
    return valores
  

def test_chi_cuadrado(secuencia=[]):
    k = 10              #Número de particiones del rango [0,1]
    longitud=1/float(k)
    list_cont=[]
    
    for i in range(0,k):
        list_cont.append(0)
                  
    for i in range(len(secuencia)):
        if secuencia[i]>0 and secuencia[i]<=longitud:
            list_cont[0]+=1
        
        elif secuencia[i]>longitud and secuencia[i]<=2*longitud:
            list_cont[1]+=1

        elif secuencia[i]>2*longitud and secuencia[i]<=3*longitud:
            list_cont[2]+=1

        elif secuencia[i]>3*longitud and secuencia[i]<=4*longitud:
            list_cont[3]+=1

        elif secuencia[i]>4*longitud and secuencia[i]<=5*longitud:
            list_cont[4]+=1

        elif secuencia[i]>5*longitud and secuencia[i]<=6*longitud:
            list_cont[5]+=1

        elif secuencia[i]>6*longitud and secuencia[i]<=7*longitud:
            list_cont[6]+=1

        elif secuencia[i]>7*longitud and secuencia[i]<=8*longitud:
            list_cont[7]+=1

        elif secuencia[i]>8*longitud and secuencia[i]<=9*longitud:
            list_cont[8]+=1

        elif secuencia[i]>9*longitud and secuencia[i]<=10*longitud:
            list_cont[9]+=1                           
        
#    for i in range(0,k):
#        print str(list_cont[i])+'\n'
        
        xi=0.0;
        
        for i in range(0,k):
            xi+=(list_cont[i]-1)*(list_cont[i]-1)
  