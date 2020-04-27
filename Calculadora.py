'''
Created on 27 abr. 2020

@author: Alfonso
'''

class Calculadora:

    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0
    
    def suma(self, valor1, valor2):
        resultado=valor1+valor2
        return resultado    
    
    def resta(self, valor1, valor2):
        resultado=valor1-valor2
        return resultado    

    def multiplicar(self, valor1, valor2):
        resultado=valor1*valor2
        return resultado
    
    def dividir(self, valor1, valor2):
        resultado=valor1/valor2
        return resultado