class Diff:
    """Classe mère pour le calcul de dérivée"""
    def __init__(self, f, h=1E-6):
        self.f = f
        self.h = float(h)



class Avant(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h) - f(x)) / h


class Arriere(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x) - f(x-h)) / h


class Central2(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h)) / 2*h


class Central4(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (4./3) * ((f(x+h)   - f(x-h))   / 2*h)\
             - (1./3) * ((f(x+2*h) - f(x-2*h)) / 4*h)


class Central6(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (3./2)  * ((f(x+h)   - f(x-h))   / 2*h)\
             - (3./5)  * ((f(x+2*h) - f(x-2*h)) / 4*h)\
             + (1./10) * ((f(x+3*h) - f(x-3*h)) / 6*h)


class Central8(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (4./5)   * ((f(x+h)   - f(x-h))   / h)\
             - (12./60) * ((f(x+2*h) - f(x-2*h)) / h)\
             + (4./105) * ((f(x+3*h) - f(x-3*h)) / h)\
             - (1./280) * ((f(x+4*h) - f(x-4*h)) / h)


class Avant3(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (-(1./6)*f(x+2*h) + f(x+h) - (1./2)*f(x) - (1./3)*f(x-h)) / h


import numpy as np

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

    def __init__(self, f, h=1E-6,type='Central',ordre=2):
        self.f = f
        self.h = float(h)
        self.type = type
        self.ordre = ordre
        self.poids = np.array(Derivation.table[(type,ordre)])

    def __call__(self,x):
        f, h = self.f, self.h
        f_valeurs = np.array([f(x+i*h) for i in range(-4,5)])
        return np.dot(self.poids,f_valeurs) / h




if __name__ == '__main__':
    # PLUS PETIT FLOATTANT EN PYTHON
    # epsilon = 2**(-52) * 2**(-1022)
    # print(epsilon)



    zt1 = lambda t: -0.5*t**2

    derivAvzt1 = Avant(zt1,h=1E-6)

    print("La dérivé en avant en {} vaut : {}".format(1,derivAvzt1(1)))
    print("La dérivé en avant en {} vaut : {}".format(2,derivAvzt1(2)))
