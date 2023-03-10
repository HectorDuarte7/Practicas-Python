#Capture nombre
n = input("Su nombre por favor: ")
#While para forzar el nombre
while n==(""):
    n = input("Su nombre por favor: ")

#Capture paterno
p = input("Su apellido paterno por favor: ")
#While para forzar el apellido paterno
while p==(""):
    p = input("Su apellido paterno por favor: ")    
    
#Capture materno
mat = input("Su apellido materno por favor: ")
#While para forzar el apellido materno
while mat==(""):
    mat = input("Su apellido materno por favor: ")  
    

#Se pide la edad que siempre es un entero por eso el int() try: 
#se inicializa la variable e
e=0
#while para forzar que se capture la edad
while (e == 0):
    try:
        e = int(input("Su edad en años por favor: "))
        print("La edad es correcta")
    except ValueError:
        e=0
        print("Escribe una edad valida")
    
#como la altura es en metros y no centimetros hay que ponerle punto y por ende es un flotante float()
#se inicializa la variable a
a = 0
while (a == 0 ):
    try:
        a = float(input("Su altura en metros por favor: "))
        
    except ValueError:
        a=0
        print("Escribe una altura valida")

#La masa en kilogramos si puede tener decimales asi que la dejamos flotante
m = 0
while (m == 0 ):
    try:
        m = float (input("Su masa en kilogramos por favor :"))
        
    except ValueError:
        m=0
        print("Escribe tu peso correcto")
#Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = m / a**2

#Le imprimos el nombre completo
print("Usuario: " + str(n) + (" ") + str(p) + (" ") + str(mat))

#Le imprimos la edad
print("Edad: " + str(e))

#Le imprimos la altura
print("Altura: " + str(a) + " mts")

#Le imprimos el peso
print("Peso: " + str(m) + " Kg")

#Le imprimos el IMC 
print("IMC: " + str(IMC) )
#Validaciones de IMC segun ISSSTE
if IMC >= 0 and IMC <= 18.49 :
    print ("Su peso es bajo")
elif IMC >= 18.50 and IMC <= 24.99 :
    print ("Su peso es normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Usted tiene sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99 :
    print ("Tiene obesidad leve")
elif IMC >= 35.00 and IMC <= 39.99:
    print ("Tiene obesidad media")
elif IMC >= 40.00:
    print ("Tiene obesidad morbida")

