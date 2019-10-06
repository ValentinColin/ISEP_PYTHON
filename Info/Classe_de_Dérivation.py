class Diff:
    """Classe mère pour le calcul de dérivée"""
    def __init__(self,f,h=10**(-6)):
        self.f = f
        self.h = float(h)



class Avant(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h) - f(h)) / h

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
        return (4./3)*((f(x+h) - f(x-h)) / 2*h)
             - (1./3)*((f(x+2*h) - f(x-2*h)) / 4*h)

class Central6(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (3./2)*((f(x+h) - f(x-h)) / 2*h)
             - (3./5)*((f(x+2*h) - f(x-2*h)) / 4*h)
             + (1./10)*((f(x+3*h) - f(x-3*h)) / 6*h)

class Central8(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (4./5)*((f(x+h) - f(x-h)) / h)
             - (12./60)*((f(x+2*h) - f(x-2*h)) / h)
             + (4./105)*((f(x+3*h) - f(x-3*h)) / h)
             - (1./280)*((f(x+4*h) - f(x-4*h)) / h)

class Avant3(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (1/h) * (-(1./6)*f(x+2*h) + f(x+h) - (1./2)*f(x) - (1./3)*f(x-h))
