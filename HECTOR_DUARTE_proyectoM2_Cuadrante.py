
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