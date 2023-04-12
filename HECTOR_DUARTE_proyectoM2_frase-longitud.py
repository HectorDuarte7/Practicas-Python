# Se solicita la palabra que se va a contabilizar
palabra = input("Introduce la palabra: ")

# Se inicia la variable size que nos permitira escribir la cantidad de letras que tendra la palabra al final
size=len(palabra)
#print(size)

#Si la palabra es de menos de 2 caracteres, se rellena con X  
if len(palabra) < 9 and len(palabra) > 3:
    palabra ="La palabra "+ palabra + " es correcta" 
    print(palabra)
else:
    if len(palabra) < 4:
        palabra = "Hacen falta letras. La palabra que ingreso solo tiene " + str(size) + " letras"
        print(palabra)
    elif len(palabra) > 8:
        palabra = "Sobran letras. La palabra que ingreso tiene " + str(size) + " letras"
        print(palabra)

    
