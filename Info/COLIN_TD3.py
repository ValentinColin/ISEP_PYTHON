# --coding:utf-8--
# COLIN Valentin
# TD3: Dérivation et intégration numériques
import numpy as np
import matplotlib.pyplot as plt


class Derivation:
    """Classe générale de dérivation"""

    table = {
    ('Avant',  1) : [0, 0, 0, 0, -1, 1, 0, 0, 0],
    ('Arriere',1) : [0, 0, 0, -1, 1, 0, 0, 0, 0],
    ('Central',2) : [0, 0, 0, -1./2, 0, 1./2, 0, 0, 0],
    ('Central',4) : [0, 0, 1./12, -2./3, 0, 2./3, -1./12, 0, 0],
    ('Central',6) : [0, -1./60, 3./20, -3./4, 0, 3./4, -3./20, 1./60, 0],
    ('Central',8) : [1./280, -4./105, 12./60, -4./5, 0, 4./5, -12./60, 4./105, -1./280],
    ('Avant' , 3) : [0, 0, 0, -2./6, -1./2, 1, -1./6, 0, 0]}

    def __init__(self,f,h=1E-6,type='Central',ordre=2):
        self.f = f
        self.h = float(h)
        self.type = type
        self.ordre = ordre
        self.poids = np.array(Derivation.table[(type,ordre)])

    def __call__(self,x):
        f, h = self.f, self.h
        f_valeurs = np.array([f(x+i*h) for i in range(-4,5)])
        return np.dot(self.poids,f_valeurs) / h

###########################  Dérivation numérique  ############################

f  = lambda x: x**3
g  = lambda x: x**2 if x>=0 else -x**2

def deriv2_central(f,x,h=1E-6):
    """Renvoie le nombre dériver de la fonction en x"""
    return (f(x+h) - f(x-h))/(2*h)

# print("Dériver centrale de f en 0",deriv2_central(f,0))
# print("Dériver centrale de g en 0",deriv2_central(g,0))

fd = Derivation(f,h=1E-9)
gd = Derivation(g,h=1E-9)

# print("Dériver centrale (classe) de f en 0",fd(0))
# print("Dériver centrale (classe) de g en 0",gd(0))


#########################  Méthode de Newton-Raphson  #########################

# Question 1:
# x(n+1) = x(n) - f(x(n)) / f'(x(n))

h  = lambda x: x**2 - 2
hd = lambda x: 2*x

# renvoie la fonction numérique tangente d'une fonction en a
# (paramètre la fonction, sa fonction dériver et le point tangent)
T  = lambda f,fd,a: (lambda x: f(a) - fd(a)*(x-a))

# Question 2:
def newt(f,fd,x0,n):
    for _ in range(n):
        # print(x0)
        x0 = x0 - f(x0)/fd(x0)
    return x0

# Question 3:
# print(newt(f=h,fd=hd,x0=2,n=10)) # 1.414213562373095

# question 4:
def newt2(f,x0,n):
    for _ in range(n):
        # print(x0)
        x0 = x0 - f(x0)/deriv2_central(f=f,x=x0)
    return x0

# print(newt2(f=h,x0=2,n=10)) # 1.414213562373095


###########################  Intégration Numérique  ###########################

# Question 1:
f = lambda x: 1/(1+x**2) # est la dériver de arctangente

def If(f,a,b):
    """Formule des trois niveaux"""
    c = (a+b)/2
    return (b-a) * ((f(a) + 4*f(c) + f(b)) / 6)

I = If(f,0,1)

# print("I              ",I) # 0.7833333333333333
# print("erreur (en %) :",(np.pi/4-I)/np.pi*100) # 0.0657 % d'erreur

# Question 2:
def simpson(f,n):
    """Calcule d'intégrale par la formule de simpson"""
    return sum([If(f,k/n,(k+1)/n) for k in range(n)])

# Question 4:
def I_rectangle(f,n):
    """Calcule d'intégrale par la méthode des rectangles médiants"""
    aire = 0
    for k in range(n):
        c = k + 0.5
        aire += 1/n * f(c/n)
    return aire
    # return sum([1/n * f((k+0.5)/n) for k in range(n)]) # version courte

print("simpson   : ",simpson(f,10))
print("rectangle : ",I_rectangle(f,10))

# Question 3:
X = list(range(1,21))
Y = [simpson(f,n) for n in X]

plt.scatter(X,Y)

axes = plt.gca()
axes.xaxis.set_ticks(range(22))
axes.set_ylim(0.7825, 0.7875)



plt.xlabel('n')
plt.ylabel('I(f)')

plt.text(1,0.7871,'f(x) = 1/(1+x^2)')

plt.title('termes de la suite des aires (formule de simpson) de f sur [0,1]')

plt.grid()
plt.show()
