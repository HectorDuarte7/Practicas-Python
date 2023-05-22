import numpy as np
import matplotlib.pyplot as plt
from random import randint
Niveles = int(12)
if Niveles >= 1:
  Contenedores = [0]*(Niveles)

for h in range((3000)):
  stored = -1
  for j in range(Niveles):
    stored += randint(0, 1)
  Contenedores[stored] += 1
print("3000 canicas se utilizaron")
print(Contenedores)
X = np.arange(-((len(Contenedores)/2)-.5), (len(Contenedores)/2)+.5)
plt.suptitle('Grafica de Galton')
plt.xlabel("Contenedores")
plt.ylabel("Cantidad de canicas por contenedor")
plt.bar(X + 0.00, Contenedores, width=0.25)
plt.show()
plt.savefig("GraficaGalton.png")