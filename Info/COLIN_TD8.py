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

plt.suptitle('2.1.6) Fonctions porte, portes, giz et cath')
plt.show()


# 2.1/2.2
plt.figure(figsize=(10,7))

Ns = [2**k for k in range(9,13)] # valeurs de N de 512 à 4096

for N in Ns:

    x = np.linspace(-8.0, 8.0, N)
    y = np.array([*map(porte,x)]) # map applique la fonction porte sur toutes les valeurs de x

    xf = np.linspace(-8.0, 8.0, N)
    yf = sc.fft(y)

    plt.plot(xf, 2.0/N * np.abs(yf[0:N]))

plt.suptitle('2.2.1/2.2.2) Spectres de la fonction porte pour différentes valeurs de N')
plt.legend(['N = {}'.format(N) for N in Ns])
plt.grid()
plt.show()


# 2.3
plt.figure(figsize=(10,7))

Ns = [2**k for k in range(9,13)] # valeurs de N de 512 à 4096

for N in Ns:

    x = np.linspace(-8.0, 8.0, N)
    y = np.array([*map(porte,x)]) # map applique la fonction porte sur toutes les valeurs de x

    yf = sc.fft(y)

    # On réorganise le spectre afin qu'il ne soit pas décalé puis on l'affiche
    plt.plot(x, 2.0/N * np.abs(np.concatenate((yf[N//2:N],yf[0:N//2]))))

plt.suptitle('2.2.3) Spectres redressés de la fonction porte pour différentes valeurs de N')
plt.legend(['N = {}'.format(N) for N in Ns])
plt.grid()
plt.show()
print("2.2.3) En effet que pour des valeurs de N pour faible, les fréquences du spectre décroissent moins vite")

# 2.4
plt.figure(figsize=(10,7))

Ns = [2**k for k in range(9,13)] # valeurs de N de 512 à 4096

for N in Ns:

    x = np.linspace(-1.0, 1.0, N)
    y = np.array([*map(porte,x)]) # map applique la fonction porte sur toutes les valeurs de x

    xf = np.linspace(-1.0, 1.0, N)
    yf = sc.ifft(sc.fft(y))

    plt.plot(xf, yf)

plt.suptitle('2.2.4) Fonction porte obtenue par transformer de fourrier inverse pour différentes valeurs de N')
plt.legend(['N = {}'.format(N) for N in Ns])
plt.grid()
plt.show()


# 2.5
plt.figure(figsize=(10,7))

N = 4096

x = np.linspace(-8.0, 8.0, N)
y = np.array([*map(portes,x)]) # map applique la fonction porte sur toutes les valeurs de x

xf = np.linspace(-8.0, 8.0, N)
yf = sc.fft(y)

plt.plot(xf, 2.0/N * np.abs(np.concatenate((yf[N//2:N],yf[0:N//2]))))

plt.suptitle('2.2.5) Spectre redressé de la fonction portes pour N = 4096')
plt.legend(['N = 4096'])
plt.grid()
plt.show()


# 2.5/2.6/2.7


N = 4096

for fonction,name in [(portes,"portes"), (cath,"cath"), (giz,"giz")]:
    plt.figure(figsize=(10,7))

    x = np.linspace(-8.0, 8.0, N)
    y = np.array([*map(fonction,x)]) # map applique la fonction porte sur toutes les valeurs de x

    xf = np.linspace(-8.0, 8.0, N)
    yf = sc.fft(y)

    plt.plot(xf, 2.0/N * np.abs(np.concatenate((yf[N//2:N],yf[0:N//2]))))

    plt.suptitle('Spectre redressé de la fonction {} pour N = 4096 (fermer la fenêtre pour voir la suite)'.format(name))
    plt.legend(['N = 4096'])
    plt.grid()
    plt.show()


# 3.1
N = 4096

plt.figure(figsize=(10,7))

X = np.linspace(-8.0,8.0,N)

Yg = np.array([*map(giz,X)])
plt.plot(X, Yg)

Yc = np.array([*map(cath,X)])
plt.plot(X, Yc)

XConv = np.linspace(-8.0,8.0,2*N-1)
delta = (8.0-(-8.0))/N # facteur d'échelle
YConv = delta * sc.convolve(Yg,Yc)
plt.plot(XConv, YConv)

plt.suptitle('2.3.1) Produit de convolution des fonction giz et cath')
plt.show()


# 3.2
N = 4096

plt.figure(figsize=(10,7))

X = np.linspace(-8.0,8.0,N)

Yg = np.array([*map(portes,X)])
plt.plot(X, Yg)

Yc = np.array([*map(cath,X)])
plt.plot(X, Yc)

XConv = np.linspace(-8.0,8.0,2*N-1)
delta = (8.0-(-8.0))/N # facteur d'échelle
YConv = delta * sc.convolve(Yg,Yc)
plt.plot(XConv, YConv)

plt.suptitle('2.3.2) Produit de convolution des fonction portes et cath')
plt.show()


# 3.3
N = 4096

plt.figure(figsize=(10,7))

X = np.linspace(-8.0,8.0,N)

Yg = np.array([*map(portes,X)])
Yc = np.array([*map(cath,X)])

Y = sc.fft(Yg) * sc.fft(Yc)

plt.plot(X, 2.0/N * np.abs(np.concatenate((Y[N//2:N],Y[0:N//2]))))


plt.suptitle('2.3.3) Spectre redresser du produit des transformer de fourier des portes et cath')
plt.show()


# 3.4
N = 4096

plt.figure(figsize=(10,7))

X = np.linspace(-8.0,8.0,N)

Yg = np.array([*map(portes,X)])
Yc = np.array([*map(cath,X)])

delta = (8.0-(-8.0))/N # facteur d'échelle
YConv = delta * sc.convolve(Yg,Yc)
Yfft  = sc.fft(YConv)
plt.plot(X, 2.0/N * np.abs(np.concatenate((Yfft[N//2:N],Yfft[0:N//2]))))

plt.suptitle('2.3.4) Spectre redresser du produit de convolution de portes et cath')
plt.show()

print("""2.3.4) Bien que ce n'est pas ce qui arrive nous devrions obtenir la même chose entre cette question et la précédente""")
