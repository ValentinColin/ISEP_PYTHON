# COLIN Valentin TD5
import time
import random as rd
import matplotlib.pyplot as plt



# 1) Fonctions récursives
# 1.1) La fonction factorielle

def f1 (n) :
    """Factorielle itérative"""
    res = 1
    for k in range (2,n+1) :
        res *= k
    return res

def f2 (n) :
    """Factorielle récursive"""
    if n == 0:
        return 1
    else :
        return f2(n-1)*n



# 1.2) La suite de Fibonacci
# question 1)

def Fibo1(n):
    """Renvoie le n-ième terme de la suite de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    F0, F1 = 0, 1
    for _ in range(2,n+1):
        F0, F1 = F1, F0+F1
    return F1

print(*["\nF1({}) = {}".format(k,Fibo1(k)) for k in range(17)])

# question 2)

def Fibo2(n):
    """Renvoie le n-ième terme de la suite de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return Fibo2(n-2) + Fibo2(n-1)

print(*["\nF2({}) = {}".format(k,Fibo2(k)) for k in range(17)])


# question 3)
""" Récursivement la fonction Fibo2 refait les mêmes calculs de plus en plus de fois lorsque n augmente
    il re-calcule plusieur fois les nombre de fibonacci inférieur pour calculer ceux supérieurs"""


# question 4)

def Fibo3(n,F0=0,F1=1):
    """Renvoie le n-ième terme de la suite de Fibonacci"""
    if n == 0:
        return F0
    elif n == 1:
        return F1
    return Fibo3(n-1,F1,F0+F1)



# 1.3) La suite de Sumer

def s1(n):
    """Suite de Sumer récursive naïve"""
    if n == 0:
        return 2
    return 0.5*(s(n-1) + 2/s(n-1))

def s2(n):
    """Suite de sumer récursive amélioré"""
    if n ==  0:
        return 2
    x = s2(n-1)
    return 0.5*(x + 2/x)


# question 1
    # ......

# question 2
    # Car dans s1, l'ordinateur fait 2 fois plus de calcul de s(n-1). Ce qui est absurde



# 1.4) L’exponentiation rapide

# question 1

def expo(x,n):
    """Exponentiation itérative"""
    result = 1
    for _ in range(n):
        result *= x
    return result

def expoR(x,n):
    """Exponentiation récursive"""
    if n == 1:
        return x
    return expoR(x,n-1) * x


# question 2

def expoRR(x,n):
    """Exponentiation rapide récursive"""
    if n == 1:
        return x
    elif n%2 == 0:
        A = expoRR(x,n//2)
        return A*A
    else:
        A = expoRR(x,(n-1)//2)
        return A*A*x



# 2) Algorithmes de tri
# 2.1) Tri aléatoire (un tri vraiment nul)

def isSort(L):
    """Test si la liste est trié par ordre croissant"""
    for k in range(len(L)-1):
        if not (L[k] <= L[k+1]):
            return False
    return True

def shuffleSort(L):
    """Tri une liste par mélange aléatoire"""
    while not isSort(L):
        rd.shuffle(L)
    return L

print("tri aléatoire de :",[0,3,1,2],"renvoie :",shuffleSort([0,3,1,2]))


# 2.2) Tri par insertion

def insertSort1(L,x=None):
    """Trie par insertion"""
    if isSort(L):
        return L
    else:
        x = L[-1]
        L = L[:-1]
        for i in range(len(L)-1,0,-1):
            if L[i] <= x:
                L.insert(i,x)
        return insertSort1(L)

def insertSort2(L,x=None):
    """Trie par insertion"""
    if x != None:
        if isSort(L):
            i = 0
            for k in range(1,len(L)):
                if L[-k] < x:
                    i = k+1
            L.insert(i,x)

    else:
        return insertSort2(L[:-1],L[-1])

def insertSort3(L,x=None):
    """Trie par insertion"""
    if len(L) <= 0:
        return L
    elif len(L) == 2:
        return [min(L),max(L)]
    else:
        if isSort(L):
            i = 0
            for k in range(1,len(L)):
                if L[-k] < x:
                    i = k+1
            L.insert(i,x)
            return L
        else:
            return insertSort3(L[:-1],L[-1])


# Ne fonctionne pas
# print("tri de :",[0,3,1,2],"renvoie :",insertSort1([0,3,1,2]))


# 2.3) Tri fusion (diviser pour mieux régner)

def split(L):
    """renvoie les 2 moitiées de liste de L"""
    n = len(L)//2
    return (L[:n],L[n:])

def mergeSort(L):
    if len(L) == 2:
        return [min(L),max(L)]
    else:
        L1,L2 = split(L)
        N = len(L)
        R = []
        for _ in range(N):
            try:
                x = min(L1[0],L2[0])
                R.append(x)
                if x in L1:
                    L1.remove(x)
                else:
                    L2.remove(x)
            except IndexError:
                if len(L1) == 0:
                    R += L2
                else:
                    R += L1
                break
        return R

# Ne fonctionne pas
# print("tri fusion de :",[0,3,1,2,8,2,5,4],"renvoie :",mergeSort([0,3,1,2,8,2,5,4]))

##############################################################
# exemple de graphique
"""
plt.title("Titre")
X = [50,100,150,200]
Y = [1,2,3,4]
plt.plot(X, Y)
plt.xlabel('abs')
plt.ylabel('ord')
plt.show()
"""
