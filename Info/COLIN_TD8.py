import math as mt
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt




# 1.1 à 1.6
def cree_liste(N):
    """Renvoie une liste de N zéros complexe"""
    return np.zeros(N,dtype=complex)

porte  = lambda x: 1 if -0.5<x<0.5 else 0
portes = lambda x: (0.8 if 0.7<x<1.7 else 1) if (-0.5<x<0.5)or(0.7<x<1.7) else 0

H = 1.234897
giz    = lambda x: (H*x+H if x<0 else -H*x+H) if -1<x<1 else 0

def cath(x):
    A = ( -0.224,  0.87)
    B = ( -0.15 ,  1.234897)
    C = ( -0.075,  0.87)
    D = (  0.224,  0.574)

    if A[0]<=x<B[0] :
        a = (B[1]-A[1])/(B[0]-A[0])
        b = A[1]-a*A[0]
        return a*x + b
    elif B[0]<=x<C[0] :
        a = (C[1]-B[1])/(C[0]-B[0])
        b = B[1]-a*B[0]
        return a*x + b
    elif C[0]<=x<D[0] :
        return D[1]
    else:
        return 0

"""
# 1.6
plt.figure(figsize=(10,7))
X = np.linspace(-8,8,4096)

plt.subplot(221)
Y = [porte(x) for x in X]
plt.plot(X, Y)

plt.subplot(222)
Y = [portes(x) for x in X]
plt.plot(X, Y)

plt.subplot(223)
Y = [giz(x) for x in X]
plt.plot(X, Y)

plt.subplot(224)
Y = [cath(x) for x in X]
plt.plot(X, Y)

plt.show()
"""
"""
# 2.1/2.2
plt.figure(figsize=(10,7))

Ns = [512,1024,2048,4096]

for N in Ns:

    x = np.linspace(-8.0, 8.0, N)
    y = np.array([*map(porte,x)])

    yf = fft(y)
    xf = np.linspace(-8.0, 8.0, N/2)

    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.suptitle('Spectre de la fonction pour différentes valeurs de N')
plt.legend(['N = {}'.format(N) for N in Ns])
plt.grid()
plt.show()
"""
