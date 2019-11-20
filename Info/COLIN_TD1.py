#    COLIN Valentin

################################# Exercice 1 #################################

result0 = 0 # initialisation de ma somme à 0
for k in range(1,51):
    result0 += k**3 # somme des cubes
# print(result0)

# print((50*51//2)**2) # formule de la somme des premier entier

################################# Exercice 2 #################################

def disco():
    """Détermine tous les nombre disco de la forme ABBA."""
    result = [] # l'ensemble des nombres disco seront stockés ici
    for A in range(1,10):
        for B in range(10):
            if A != B:
                nbr = A*10**3 + B*10**2 + B*10 + A
                if nbr in [n**2 for n in range(100)]:
                    result.append(nbr)
    return result

# l'antislash en fin de ligne permet de couper la ligne de code comme un retour à la ligne
def disco_opti():
    """Détermine tous les nombre disco de la forme ABBA."""
    result = []
    for carre in [n**2 for n in range(int(1000**0.5)+1,100)]:
        if (str(carre)[0] == str(carre)[3]) \
            and (str(carre)[1] == str(carre)[2]) \
            and (str(carre)[0] != str(carre)[1]):
            result.append(carre)
    return result

# print(disco(),disco_opti()) # il y en a aucun

def hard_rock():
    """Détermine tous les nombre hard rock de la forme ACDC."""
    result = [] # l'ensemble des nombres hard rock seront stockés ici
    for A in range(1,10):
        for C in range(10):
            for D in range(10):
                if A != C and A != D and C != D:
                    nbr = A*10**3 + C*10**2 + D*10 + C
                    if nbr in [n**2 for n in range(100)]:
                        result.append(nbr)
    return result

# l'antislash en fin de ligne permet de couper la ligne de code comme un retour à la ligne
def hard_rock_opti():
    """Détermine tous les nombre disco de la forme ABBA."""
    result = []
    for carre in [n**2 for n in range(int(1000**0.5)+1,100)]:
        if (str(carre)[1] == str(carre)[3]) and (str(carre)[0] != str(carre)[1]) \
        and (str(carre)[0] != str(carre)[2]) and (str(carre)[1] != str(carre)[2]):
            result.append(carre)
    return result

# print(hard_rock(),hard_rock_opti()) # [3969, 5929, 8464]

################################# Exercice 3 #################################

def syracuse(u0):
    """Renvoie le plus petit indice n tel que le terme u(n) = 1"""
    n = 0
    while u0 > 1:
        if u0%2 == 0: # si n est pair
            u0 //= 2
        else:         # sinon
            u0 = 3*u0 + 1
        n += 1
    return n

# print(syracuse(15)) # 17

################################# Exercice 4 #################################

# la fonction map(f,L) renvoie la liste des images de chaque élément de la liste L par la fonction f
def amstrong(max=10000):
    """Renvoie tous les nombres d'Amstrong inférieur au max."""
    result = []
    for N in range(max+1):
        N_list = map(int,str(N))
        if sum(map(lambda x: x**3, N_list)) == N: # vérifie si la somme des cubes des chiffre de N est égal à N
            result.append(N)
    return result

# print(amstrong()) # [0, 1, 153, 370, 371, 407]

################################# Exercice 5 #################################

def nbr_apocalyptique():
    """Renvoie le plus petit nombre apocalyptique
    dans la suite des puissance de 2."""
    n = 0
    while not('666' in str(2**n)): # Tant que l'on a pas trouvé la séquence '666' dans la puissance de 2, on continue
        n+=1
    return 2**n

# print(nbr_apocalyptique()) # 182687704666362864775460604089535377456991567872

################################# Exercice 6 #################################

def courbe_elliptique(inter=[1000,1001]): # solutions entière
    """Détermine les solution de l'équation y**2 = x**3 + x + 1
    à une précision err."""
    solutions = []
    for y in range(-inter[0],inter[1]):
        for x in range(-inter[0],inter[1]):
            if y**2 == x**3 + x + 1:
                solutions.append((x,y))
    return solutions

def courbe_elliptique2(inter=[1000,1001],err=10**-3): # solutions floattante
    """Détermine les solution de l'équation y**2 = x**3 + x + 1
    à une précision err, en cherchant les solutions dans l'intervalle inter"""
    solutions = []
    for y in range(-inter[0],inter[1]):
        for x in range(-inter[0],inter[1]):
            if abs((y*err)**2 - ((x*err)**3 + (x*err) + 1)) < err:
                solutions.append((x*err,y*err))
    return solutions

# print(courbe_elliptique())
# print(courbe_elliptique2())

################################# Exercice 7 #################################

def permutations(liste):
    """Prend en argument une liste (pas de tuple)
    renvoie la liste des permutation d'une liste.
    Mais attention la taille de la liste renvoyer
    est en factorielle."""
    if len(liste) == 2:
        return [(liste[0],liste[1]), (liste[1],liste[0])]
    else:
        result = []
        for i in range(len(liste)):
            b = liste[:]
            del b[i]
            result += [tuple([liste[i]])+a for a in permutations(b)]
        return result

def enigme():
    nombres_init = [2,3,4,5]
    operations_init = ['+','-','*','/']
    dict_opera = {  '+' : lambda x,y: x+y,
                    '-' : lambda x,y: x-y,
                    '*' : lambda x,y: x*y,
                    '/' : lambda x,y: x/y}
    res = 26
    solutions = []
    for nombres in permutations(nombres_init):
        for operations in permutations(operations_init):
            a,b,c,d = nombres[0],nombres[1],nombres[2],nombres[3]
            f,g,h = operations[0],operations[1],operations[2] # pas besoins de regarder la dernière opérations puisqu'elle ne sera pas utilisé
            f,g,h = dict_opera[f],dict_opera[g],dict_opera[h] # se sont maintenant des fonctions
            # print(h(g(f(a,b),c),d),"((({0} {4} {1}) {5} {2}) {6} {3})".format(a,b,c,d,operations[0],operations[1],operations[2]))
            if h(g(f(a,b),c),d) == res:
                solutions.append("((({0} {4} {1}) {5} {2}) {6} {3})".format(a,b,c,d,operations[0],operations[1],operations[2]))
    return ("Il y a {} Solution(s)".format(len(solutions)),solutions)

# print(enigme()) # ('Il y a 1 Solution(s)', ['(((3 / 2) + 5) * 4)'])

################################# Exercice 8 #################################
###  MOCHE (mais fonctionne)

def no_occurrence(liste):
    """Vérifie s'il n'y à pas de doublon dans la liste
    si il y en a --> renvoie False,
    Sinon renvoie True."""
    for k in liste:
        if liste.count(k) > 1:
            return False
    return True

def cryptarithme():
    """Résout le cryptarithme 'UN + UN + NEUF = ONZE'.
    Où chaque lettre est un chiffre, tous distinct les uns des autres."""
    res_str = []
    for E in range(10):  # E F N O U Z
        for F in range(10):
            for N in range(1,10):
                for O in range(1,10):
                    for U in range(1,10):
                        for Z in range(10):
                            if no_occurrence([E,F,N,O,U,Z]): # permet de vérifié que les valeurs des lettres sont bien 2 à 2 distincts
                                if 2 * (U*10+N) + N*10**3+E*10**2+U*10+F == O*10**3+N*10**2+Z*10+E:
                                    res_str.append("{4}{2} + {4}{2} + {2}{0}{4}{1} = {3}{2}{5}{0}".format(E,F,N,O,U,Z))
                                    res_str.append("E = {}, F = {}, N = {}, O = {}, U = {}, Z = {}".format(E,F,N,O,U,Z))
                                    # juste pour le confort de lire le résultat
    return res_str

# print(cryptarithme())
