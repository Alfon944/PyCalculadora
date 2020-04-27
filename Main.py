'''
Created on 26 abr. 2020

@author: Alfonso
'''
from calculadora.Calculadora import Calculadora

#funciones de la aplicacion
#menu
def mostrarMenu():
    print("**MENU**")
    print("1--SUMA--")
    print("2--RESTA--")
    print("3--MULTIPLLICAR--")
    print("4--DIVIDIR--")
    print("5--SALIR--")
#metodo selector de mensajes
def diccionarioTexto(argumento):
    opcion = {
        0: "selecciones una opcion",
        1: "opcion incorrecta",
        2: "Escoga una opcion...",
        3: "",
        4: "Introduce valor 1",
        5: "Introduce valor 2"
    }
    print(opcion.get(argumento, "No hay valor"))
#metodo de entrada de datos numericos
def entradaNum(opcion):
    while True:
        valor=input(diccionarioTexto(opcion))
        try:
            valor=int(valor)
            return valor
        except ValueError:
            print("Valor entrada no numerico")
            
#inicio de aplicacion
if __name__ == '__main__':
    pass
'''creacion objeto calculadora'''
c=Calculadora()

while True:
    mostrarMenu()
    diccionarioTexto(3)
    valor=entradaNum(0)
    if valor>=0 and valor<=4:
        if valor>=0 and valor<=4:
            if valor==1:
                valor1=entradaNum(4)
                valor2=entradaNum(5)
                print(c.suma(valor1, valor2))
            elif valor==2:
                valor1=entradaNum(4)
                valor2=entradaNum(5)
                print(c.resta(valor1, valor2))
            elif valor==3:
                valor1=entradaNum(4)
                valor2=entradaNum(5)
                print(c.multiplicar(valor1, valor2))
            elif valor==4:
                valor1=entradaNum(4)
                valor2=entradaNum(5)
                print(c.dividir(valor1, valor2))
    elif valor==5:
        break
    else:
        print("Opcion no disponible")
        break
print("Aplicacion finalizada!")