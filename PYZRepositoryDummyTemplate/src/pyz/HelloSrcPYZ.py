# -*- coding: utf-8 -*-

'''
Created on 22.11.2026

@author: Fritz Lindhauer
'''

class HelloSrcPYZ:
    def __init__(self):
       pass
    
    def compute(self, sString):
        return "Src: Hallo " + sString
        
    
# Code zum Test am Schluss, nur wenn diese Klasse direkt gestartet wird
if __name__ == "__main__":
    #Instanziere die Klasse mit dem passenden Namen
    hallo = HelloSrcPYZ()
    erg01 = hallo.compute('Welt')
    print(erg01) 
    
   
    
    