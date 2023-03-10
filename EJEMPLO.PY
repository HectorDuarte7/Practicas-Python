"""
	Validar si una cadena o variable es un entero
	en Python
	@author parzibyte
"""
# Nota: la variable podría venir de cualquier lado, en
# este caso el usuario la escribe
posible_numero = input("Escribe algo y te diré si es un entero: ")
try:
	entero = int(posible_numero)
	print("Lo que escribiste es un entero")
except ValueError:
	print("Lo que escribiste NO es un ent