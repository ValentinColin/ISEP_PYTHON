from math import sqrt

################################# Exercice 1 #################################

result0 = 0
for k in range(1,51):
    result0 += k**3 # somme des cubes
# print(result0)

# print((50*51//2)**2)

################################# Exercice 2 #################################

def disco():
    """Détermine tous les nombre disco"""
    result = []
    for A in range(1,10):
        for B in range(10):
            if A != B:
                nbr = A*10**3 + B*10**2 + B*10 + A
                if (sqrt(nbr)).is_integer():
                    result.append(nbr)
    return result

# print(disco()) # il y en a aucun

def hard_rock():
    """Détermine tous les nombre hard rock"""
    result = []
    for A in range(1,10):
        for C in range(10):
            for D in range(10):
                if A != C and A != D and C != D:
                    nbr = A*10**3 + C*10**2 + D*10 + C
                    if (sqrt(nbr)).is_integer(): # ou if int(sqrt(nbr)) == sqrt(nbr):
                        result.append(nbr)
    return result

# print(hard_rock()) # [3969, 5929, 8464]

################################# Exercice 3 #################################

def syracuse(u0):
    """renvoie le plus petit indice n tel que le terme u(n) = 1"""
    n = 0
    while u0 > 1:
        if u0%2 == 0:
            u0 //= 2
        else:
            u0 = 3*u0 + 1
        n += 1
    return n

# print(syracuse(15)) # 17

################################# Exercice 4 #################################

def amstrong(max=10000):
    """renvoie tous les nombres d'Amstrong inférieur au max."""
    result = []
    for N in range(max+1):
        N_list = map(int,str(N)) # map(f, L) applique la fonction f à tous les éléments de la liste L et renvoie la liste des images de f
        if sum(map(lambda x: x**3, N_list)) == N: # vérifie si la somme des cubes des chiffre de N est égal à N
            result.append(N)
    return result

# print(amstrong())

################################# Exercice 5 #################################

def nbr_apocalyptique():
    """Renvoie le plus petit nombre apocalyptique
    dans la suite des puissance de 2."""
    n = 0
    while True: # Tant que l'on a pas trouvé la séquence '666' dans la puissance de 2, on continue
        n+=1
        if '666' in str(2**n):
            break
    return 2**n

# print(nbr_apocalyptique()) # 182687704666362864775460604089535377456991567872

################################# Exercice 6 #################################



################################# Exercice 7 #################################

def permutations(liste):
    """Prend en argument une _liste (pas de tuple)
    renvoie la _liste des permutation d'une _liste
    mais attention la taille de la _liste renvoyer
    est en !n ->factorielle "le nombre l'élément" """
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
    res = 26
    for nombres in permutations(nombres_init):
        for operations in permutations(operations_init):
            pass


################################# Exercice 8 #################################
### EST TRÈS MOCHE (mais fonctionne)

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
                            if E!=F and E!=N and E!=O and E!=U and E!=Z:
                                if F!=N and F!=O and F!=U and F!=Z:
                                    if N!=O and N!=U and N!=Z:
                                        if O!=U and O!=Z:
                                            if U!=Z:
                                                if 2 * (U*10+N) + N*10**3+E*10**2+U*10+F == O*10**3+N*10**2+Z*10+E:
                                                    res_str.append("{4}{2} + {4}{2} + {2}{0}{4}{1} = {3}{2}{5}{0}".format(E,F,N,O,U,Z))
                                                    # res_str.append(str(U*10+N)+' + '+str(U*10+N)+' + '+str(N*10**3+E*10**2+U*10+F)+' = '+str(O*10**3+N*10**2+Z*10+E))
    return res_str


# print(cryptarithme())
