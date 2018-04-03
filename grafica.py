import numpy as num 
import matplotlib.pyplot as plt

datos = num.loadtxt('datos.txt')
x = datos[:,0]
y = datos[:,1]

plt.plot(x, y)
plt.title("No. sobres vs repetidas")
plt.xlabel("Laminas repetidas")
plt.ylabel("No. sobres")
plt.savefig("Laminas")
