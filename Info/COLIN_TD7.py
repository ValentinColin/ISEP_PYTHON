import matplotlib.pyplot as plt
from math import pi

print("""
GRAPHES
1)a) (graphe orienté)
sommet :    1   2   3   4   5
degré  :    2   1   2   0   1

b) matrice d'adjacence:
[[0,1,0,1,0],
 [1,0,0,0,0],
 [1,0,0,0,1],
 [0,0,0,0,0],
 [0,0,0,1,0]]

c) Les sommets 2 et 3 ne sont pas reliés par un chemin,
le graphe n'est donc pas complet

d) Le graphe sous-jacent est connexe car tous les sommets peuvent être reliés par un chemin

e)
V = [1,2,3,4,5]
E = [(1,2),(1,4),(2,1),(3,1),(3,5),(5,4)]
G = [V,E]
""")

# 2)
# si E est définie par une liste de couple
def degreOr(E,x):
    """Renvoie le degré du sommet x dans un graphe orienté"""
    count = 0
    for a in E:
        if x == a[0]:
            count += 1
    return count

def degreNOr(E,x):
    """Renvoie le degré du sommet x dans un graphe non orienté
    (les boucles étant comptés double)"""
    count = 0
    for a in E:
        if x == a[0]:
            count += 1
        if x == a[1]:
            count += 1
    return count


# 3)
# Il s'agit de la matrice D'ADJACENCE et non d'incidence
def matAdj(V,E):
    """Renvoie la matrice d'adjacence du graphe (quelconque)
    exemple: V = [1,2,3]   E = [(1,2),(2,3),(3,3)]   mat = [[0,1,0],
                                                            [0,0,1],
                                                            [0,0,1]]"""
    n = len(V)
    mat = [[0 for j in range(n)] for i in range(n)]
    for i,j in E:
        mat[i-1][j-1] += 1
    return mat

# 4)
def graphe(Mat):
    """Renvoie le graphe simple correspondant à la matrice"""
    n = len(mat)
    V = [i+1 for i in range(n)]
    E = []
    for i in range(n):
        for j in range(n):
            if Mat[i][j] >= 1:
                E.append((i+1,j+1))
    return V,E

# 5)
def K(n):
    """Renvoie le graphe complet à n sommets"""
    V = [i+1 for i in range(n)]
    E = []
    for j in range(1,n+1):
        for i in range(1,j+1):
            if {i,j} not in E and i != j:
                E.append([i,j])
    return V,E


# 6)
def list_segment(n):
    """Permet d'avoir les couples arguments (non consécutif) à relié
    dans le graphe complet à n sommets
    afin de le représenté sous la forme d'un polygone régulier à n cotés"""
    arg = [k*2*pi/n for k in range(n)]
    S = []
    theta = 2*pi/n
    for k in range(n) :
        if k == 0:
            for l in range(2,n-1):
                S += [(1,k*theta),(1,l*theta)]
        elif k == n-1:
            for l in range(1,n-2):
                S += [(1,k*theta),(1,l*theta)]
        else:
            for l in [i for i in range(k-1)]+[i for i in range(k+2,n)]:
                S += [(1,k*theta),(1,l*theta)]
    # print("S:",S)
    return S

def repK(n):
    """Représente le graphe K(n) quand ses sommets
    sont ceux d’un polygone régulier à n côtés."""
    plt.suptitle("Graphe complet à {} sommets".format(n))

    theta = 2*pi/n
    Points = [(1,k*theta) for k in range(n)]
    Points.append(Points[0])

    X1, Y1 = zip(*Points)   # zip('ab', 'cd', 'ef') --> ace bdf
    X2, Y2 = zip(*list_segment(n))
    # print("X1",X1,"et Y1",Y1)
    # print("X2",X2,"et Y2",Y2)

    plt.polar(Y1,X1,Y2,X2,color="blue")
    plt.show()

repK(12)

# 7)
def adj(s,E):
    """Renvoie la liste des sommets adjacent"""
    L = []
    for i,j in E:
        if i == s:
            L.append(j)
    return L

def est_connexe(V,E):
    """Méthode naïve pour vérifier si un graphe (non orienté) est connexe"""
    saw = V[0]
    for S0 in saw:
        for Si in adj(S0,E):
            if not Si in saw:
                saw.append(Si)
    return len(saw) == len(V)

# Arbres Binaires
print("Arbre Binaires")
print("""1)a)
La hauteur de l'arbre est 4-1 = 3
b) [1,     [2,  [3,[],[]]  ,[4,[],[]]],       [5,  [6,  [7,[],[]],  []],  []]]
""")

# 2)
def est_vide(a):
    """Test si l'arbre binaire est vide"""
    return a == []

# 3)
def etiquette(a):
    """Renvoie la racine de l'arbre binaire"""
    return a[0]

# 4)
def Fg(a):
    """Renvoie le fils gauche de l'arbre binaire"""
    return a[1]

def Fd(a):
    """Renvoie le fils droit de l'arbre binaire"""
    return a[2]

# 5)
def feuilles(a):
    """Renvoie la liste des feuilles de l'arbre binaire de manière récursive"""
    F = []
    # Cas de base
    if est_vide(Fg(a)) and est_vide(Fg(a)):
        F.append(a)

    # Cas récursif
    if not est_vide(Fg(a)):
        F += feuilles(Fg(a))
    if not est_vide(Fd(a)):
        F += feuilles(Fd(a))

    return F

# 6)
def h(a):
    """Renvoie la hauteur de l'arbre binaire non vide"""
    if est_vide(a):
        raise ValueError
    # Cas de base
    if est_vide(Fg(a)) and est_vide(Fd(a)):
        return 0

    # Cas récursif
    g = 1
    if not est_vide(Fg(a)) and not est_vide(Fd(a)):
        g += max(h(Fg(a)), h(Fd(a)))
    elif not est_vide(Fg(a)):
        g += h(Fg(a))
    else:
        g += h(Fg(a))

    return g

"""
A = [1,     [2,  [3,[],[]]  ,[4,[],[]]],       [5,  [6,  [7,[],[]],  []],  []]]
B = [1, [2,[3,[],[]],[]], []]
print("hauteur de A:",h(A)," avec A =",A)
print("hauteur de B:",h(B)," avec B =",B)
"""


def expr(a):
    """ne fonctionne pas"""
    # case de base
    if est_vide(Fg(a)) and est_vide(Fd(a)):
        if etiquette == 0:
            return
        return etiquette(a)

    # case récursif
    P = etiquette(a)
    if P == 1:  P = ""
    else:       P = " x {}".format(P)

    g, d = expr(Fg(a)), expr(Fd(a))
    if g != 0 and d != 0:
        if int(d) < 0:
            S = "({} - {})".format(str(g),str(abs(d)))
        else:
            S = "({} + {})".format(str(g),str(d))
    elif g != 0 and d == 0:
        S = str(g)
    elif g == 0 and d != 0:
        S = str(d)
    else:
        S = ""

    return S + P

# E = "(" + expr(Fg(a)) + "+" + expr(Fd(a)) + ")" + "x" + P


C = [1,[2,[1,[],[]],[-3,[],[]]],[1,[4,[],[]],[5,[5,[],[]],[0,[],[]]]]]
# print(expr(C))

# 8)
def parcours_pref(a):
    """Parcours en profondeur avec ordre préfixé"""
    sommets = [etiquette(a)]
    # cas de base
    if est_vide(Fg(a)) and est_vide(Fd(a)):
        return sommets

    # cas récursif
    if not est_vide(Fg(a)):
        sommets += parcours_pref(Fg(a))
    if not est_vide(Fd(a)):
        sommets += parcours_pref(Fd(a))

    return sommets


print("Parcours en profondeur avec ordre préfixé (de l'arbre en introduction):",parcours_pref(A))
