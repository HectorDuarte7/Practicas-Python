Lo primero que hice fue analizar los ejemplos que nos habian dado para identificar la forma en que trabajaban los programas.

Posteriormente lei las instrucciones y fui desarrollando lo que se solicitaba paso a paso.
# Se llama la libreria os
import os

#Se pide el valor de X que siempre es un entero por eso el int() try: 
#se inicializa la variable x
x=0
#while para forzar que x sea diferente de 0
while (x == 0):
    try:
        x = int(input("Escriba el valor de X que no sea 0: "))
        
    except ValueError:
        x=0
        print("Debe escribir solo enteros")
    
#Se pide el valor de Y que siempre es un entero por eso el int() try: 
#se inicializa la variable y
y = 0
while (y == 0 ):
    try:
        y = int(input("Escriba el valor de Y que no sea 0: "))
        
    except ValueError:
        y=0
        print("Debe escribir solo enteros")
        
        
# Se realiza la validacion de los datos X,Y para identificar el cuadrante
if x>0 and y>0:
    print ('Las coordenadas se encuentran en el cuadrante I')
if x<0 and y>0:
    print ('Las coordenadas se encuentran en el cuadrante II')
if x<0 and y<0:
    print ('Las coordenadas se encuentran en el cuadrante III')
if x>0 and y<0:
    print ('Las coordenadas se encuentran en el cuadrante IV')

os.system ('pause')

# Se solicita la palabra que se va a contabilizar
palabra = input("Introduce la palabra: ")

# Se inicia la variable size que nos permitira escribir la cantidad de letras que tendra la palabra al final
size=len(palabra)
#print(size)

#Se realizan las validaciones de acuerdo a las instrucciones
#si la palabra tiene menos de 9 letras pero mas de 3 se considera correcta 
if len(palabra) < 9 and len(palabra) > 3:
    palabra ="La palabra "+ palabra + " es correcta" 
    print(palabra)
#si la palabra no cumple con las caracteristicas anteriores se realiza la validacion del tamaño
else:
    #si la palabra es menor de 4 letras se indica que faltan letras
    if len(palabra) < 4:
        palabra = "Hacen falta letras. La palabra que ingreso solo tiene " + str(size) + " letras"
        print(palabra)
    #si la palabra es mayor de 8 letras se indica que sobran letras    
    elif len(palabra) > 8:
        palabra = "Sobran letras. La palabra que ingreso tiene " + str(size) + " letras"
        print(palabra)


Ahora que ha avanzado el bootcamp me parece que los contenidos han sido adecuados, igual que las practicas las cuales han permitido usar los conocimientos adquiridos.