Lo primero que hice fue analizar el ejemplo que nos habian dado para identificar la forma enq ue trabajaba el programa.
Posteriormente lei las instrucciones y fui desarrollando lo que se solicitaba paso a paso.
La primera linea solicita el nombre del usuario
n = input("Su nombre por favor: ")

Posteriormente utilizo un while para forzar a que se escriba un nombre, si el usuario no escribe nada el programa continuara pidiendo el nombre del usuario.

#While para forzar el nombre
while n==(""):
    n = input("Su nombre por favor: ")

El nombre del usuario se guarda en la variable n

Se repite la operacion para los apellidos paterno y materno.
p = input("Su apellido paterno por favor: ")
while p==(""):
    p = input("Su apellido paterno por favor: ")    
    
mat = input("Su apellido materno por favor: ")
while mat==(""):
    mat = input("Su apellido materno por favor: ") 

Los apellidos del usuario se guardan en las variable p para el apellido paterno y mat para el apellido materno.

Una vez que se han registrado los datos del usario procedemos al siguiente paso que es solicitar la edad. 
    
La edad la solicitamos como un valor entero por eso usamos int, al principio me marcaba un error al tratar de usar el operador try por lo que decidi integrarlo en un ciclo while, el cual no reconocia la variable e, es por eso que la inicialice antes del ciclo, si el usuario escribe en decimales o coloca un caracter que no sea entero envia un mensaje de erro y reinicializamos la variable para que continue el ciclo while

#Se pide la edad que siempre es un entero por eso el int() 
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
 
Se repite la misma operacion para la altura y la masa solo que en este caso si permitimos decimales por lo que utilizamos float en vez de int  

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

Se calcula el IMC  de acuerdo a la formula pasando los valores de las variables m y a el resultado se guarda en la varible IMC

#Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = m / a**2

Posteriormente procedemos a imprimir en pantalla todos los valores que recolectamos concatenando el nombre el apellido paterno y el apellido materno con espacios entre ellos para mejorar la visibilidad.

#Le imprimos el nombre completo
print("Usuario: " + str(n) + (" ") + str(p) + (" ") + str(mat))


Imprimimos tambien  la edad, la altura y el peso asi como el IMC que habiamos obtenido y de acuerdo a la tabla que se nos proporciono imprimimos tambien el grado de obesidad en el que se encuentra el usuario.

#Le imprimos la edad
print("Edad: " + str(e))

#Le imprimos la altura
print("Altura: " + str(a) + " mts")

#Le imprimos el peso
print("Peso: " + str(m) + " Kg")

#Le imprimos el IMC 
print("IMC: " + str(IMC) )

Para obtener el grado de obesidad del usuario validamos utilizando operador if y elif comparando el IMC calculado anteriormente e imprimimos en pantalla el dato resultante.

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

Hasta el momento el bootcamp me ha parecido sencillo y concreto, he podido recordar muchas cosas que ya no utilizaba, por supuesto me tope con algunos detalles que no habia captado en la sesion como por ejemplo la indentacion del lenguaje que me causo un poco de problemas al momento de estar desarrollando la aplicacion y la sintaxis de los operadores, aunque muchas de las dudas que tenia se resolvieron durante la sesion de clase.