# COLIN Valentin TD3
import numpy as np
import matplotlib.pyplot as plt

###########################  Dérivation numérique  ############################

class Derivation:
    """Classe de dérivation"""

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


#########################  Méthode de Newton-Raphson  #########################

# Question 1:
# x(n+1) = x(n) - f(x(n)) / f'(x(n))

# Question 2:
def newt(f,f_deriver,x0,n):
    """Renvoie une solution approcher de f(x)=0,
    par la méthode de Newton-Raphson après n itération"""
    for _ in range(n):
        x0 = x0 - f(x0)/f_deriver(x0)
    return x0

# Question 3:
h  = lambda x: x**2 - 2
hd = lambda x: 2*x

# print("Valeur approcher de racine de 2 :",newt(h,hd,2,20)) # 1.414213562373095

# Question 4:
def newt2(f,x0,n):
    """Renvoie une solution approcher de f(x)=0,
    par la méthode de Newton-Raphson après n itération"""
    fd = Derivation(f,h=1E-6,type='Central',ordre=2)
    for _ in range(n):
        x0 = x0 - f(x0)/fd(x0)
    return x0

# print("Valeur approcher de racine de 2 :",newt2(h,2,20)) # 1.414213562373095


###########################  Intégration Numérique  ###########################

class Fonctions:
    """Classe de fonctions"""

    @staticmethod
    def I(fonction,segment):
        """Formule des trois niveaux"""
        a,b = segment[0],segment[1]
        c = (a+b)/2
        return (b-a) * ((f(a) + 4*f(c) + f(b)) / 6)

    def __init__(self,f,borne=[0,1]):
        self.f = f
        self.borne = [min(borne),max(borne)]

    def __call__(self,x):
        """Si x est dans l'intervalle de définition de self,
        renvoie l'évaluation de f en x"""
        a,b = self.borne
        if a <= x <= b:
            return self.f(x)
        else:
            raise ValueError("{} is not in the interval {}".format(x,self.borne))

    def simpson(self,n):
        """Calcule d'intégrale par la formule de simpson"""
        return sum([Fonctions.I(self.f,[k/n,(k+1)/n]) for k in range(n)])

    def rectangles_inf(self,n):
        """Calcule d'intégrale par la méthode des rectangles"""
        a,b = self.borne
        return sum([1/n * self((k/n)*a + (1-(k/n))*b) for k in range(n)])

    def rectangles_sup(self,n):
        """Calcule d'intégrale par la méthode des rectangles"""
        a,b = self.borne
        return sum([1/n * self((k/n)*a + (1-(k/n))*b) for k in range(n)])

    def rectangles_medians(self,n):
        """Calcule d'intégrale par la méthode des rectangles médiants"""
        a,b = self.borne
        return sum([1/n * self((k/n)*a + (1-(k/n))*b) for k in range(n)])



if __name__ == '__main__':
    # Partie 1:

    # Fonctions
    f = lambda x: x**3
    g = lambda x: x**2 if x >= 0 else -x**2

    # Fonctions Dérivés
    fd = Derivation(f,h=1E-6,type='Central',ordre=2)
    gd = Derivation(g,h=1E-6,type='Central',ordre=2)

    print("Dériver centrale de f en 0 :",fd(0)) # 1e-12
    print("Dériver centrale de g en 0 :",gd(0)) # 1e-06


    # Partie 2:

    # Question 1:
    # x(n+1) = x(n) - f(x(n)) / f'(x(n))

    # Question 3:
    print("Valeur approcher de racine de 2 :",newt(h,hd,2,20)) # 1.414213562373095

    # Question 4:
    print("Valeur approcher de racine de 2 :",newt2(h,2,20)) # 1.414213562373095


    # Partie 3:

    # Question 1:
    f = Fonctions(lambda x: 1/(1+x**2),[0,1]) # fonction dériver de arctangente
    If = Fonctions.I(f,[0,1])

    print("Intégrale de f sur [0,1]",If) # 0.7833333333333333
    print("La valeur exacte de l'intégrale étant pi/4 on a une erreur (en %) de :",(np.pi/4-If)/(np.pi/4)*100)
    # 0.2629 % d'erreur

    # Question 3:
    # voir à la fin du fichier pour voir le script de l'affichage du nuage de point

    # Question 4:
    print("simpson   : ",f.simpson(n=20))
    print("rectangle : ",f.rectangles_medians(n=20))


    # Question 3:
    X = list(range(1,21))
    Y = [f.simpson(n) for n in X]

    plt.scatter(X,Y)

    axes = plt.gca()
    axes.xaxis.set_ticks(range(22))
    axes.set_ylim(0.7825, 0.7875)

    plt.xlabel('n')
    plt.ylabel('I(f)')

    plt.text(1,0.7871,'f(x) = 1/(1+x^2)')

    plt.title('Termes de la suite des intégrales sur [0,1] (formule de simpson) de f')

    plt.show()
