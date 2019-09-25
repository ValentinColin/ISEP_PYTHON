import numpy as np
import matplotlib.pyplot as plt

# définition des alias de constantes
e  = np.e
pi = np.pi

################ CALCUL DES RAPPORTS ################

def facto(n):
    """Permet de calculer récursivement la factoriel de n."""
    if n > 1:
        return n * facto(n-1)
    else:
        return 1

rapport0 = lambda n : facto(n) / ((n/e)**n * (2*pi*n)**0.5)
rapport1 = lambda n : facto(n) / ((n/e)**n * (2*pi*n)**0.5 * (1 + 1/(12*n)))


############### AFFICHAGE DES COURBES ###############

x = [n for n in range(10,151)]
y1 = [rapport0(n) for n in x]
y2 = [rapport1(n) for n in x]

plt.plot(x, y1, ".", label="rapport à l'ordre 0", linewidth=1)
plt.plot(x, y2, ".", label="rapport à l'ordre 1", linewidth=1)
plt.xticks([10*n for n in range(1,16)], [10*n for n in range(1,16)])

plt.title("Comparaison des rapports des formules de Stirling à l'ordre 0 et 1")
plt.legend()

plt.xlabel("n")
plt.ylabel("Rapports")

plt.show()
