""" ###########################################################################
Soit une chaine de caractères :
Ecrire un algorithme récursif permettant de déterminer sa longueur
"""

def longueur(list):
    """Détermine la longueur d'une liste de façon récursive"""
    if not(list):
        return 0
    else:
        return 1+longueur(list[1:])


""" ###########################################################################
Rendre récursive la fonction somme suivante :
def somme(list):
    sum = 0
    for value in list :
        sum += value
    return sum
"""

def somme_recu(list):
    if not(list):
        return 0
    else:
        return list[0] + somme_recu(list[1:])


""" ###########################################################################
Pour convertir un nombre entier positif N de la base décimale à la base binaire,
il faut opérer par des divisions successives du nombre N par 2.
Les restes des divisions constituent la représentation binaire.

Ecrire une fonction récursive « Binaire » permettant
d’imprimer à l’écran la représentation binaire d’un nombre N
(voir exemple en face).
"""

def binaire(N):
    if N==0:
        return []
    return binaire(N//2)+[N%2]


""" ###########################################################################
La suite de Fibonacci est définie comme suit :

U(n) { 1 si n < 2
       U(n-1) + U(n-2) sinon

Ecrire un programme récursif permettant de calculer le nième terme de la suite;
"""

def fib(N):
    """Renvoie le terme U(N) de la suite de fibonacci avec U(0)=U(1)=1"""
    if N < 2:
        return 1
    else:
        return fib(N-1)+fib(N-2)


""" ###########################################################################
La suite de Fibonacci est définie comme suit :
(méthode à ne jamais faire en pratique)

U(n) { 1 si n < 2
       3U(n-1) + U(n-2) sinon

Ecrire un programme récursif permettant de calculer le nième terme de la suite;
"""

def suite(N):
    """Renvoie le terme U(N) de la suite écrite 'au dessus' avec U(0)=U(1)=1 """
    if N < 2:
        return 1
    else:
        return 3*suite(N-1)+suite(N-2)


""" ###########################################################################
Un nombre N est pair si (N-1) est impair,
et un nombre N est impair si (N-1) est pair.
Ecrire deux fonctions récursives mutuelles pair (N) et impair (N)
permettant de savoir si un nombre N est pair et si un nombre N est impair.
"cette récursivité fonctionne au max jusqu'au nombre 999 exclus"
"""

def pair(N):
    if N==1:
        return False
    else:
        return impair(N-1)

def impair(N):
    if N==1:
        return True
    else:
        return pair(N-1)


""" ###########################################################################
Soit un tableau 'Tab' de 'n' entiers.
Ecrire une fonction récursive simple permettant de déterminer
le maximum du tableau
"""

def maximum(Tab):
    if len(Tab)==1:
        return Tab[0]
    else:
        M = len(Tab)//2
        max1 = maximum(Tab[:m])
        max2 = maximum(Tab[m:])
        if max1 > max2:
            return max1
        else:
            return max2


""" ###########################################################################
Un tableau X est trié par ordre croissant si x(i)<=x(i+1) pour i
Elaborer un algorithme récursif permettant de vérifier
qu’un tableau X est trié ou non
"""

def test_tri(Tab):
    if len(Tab) < 2:
        return True
    elif len(Tab) == 2:
        return Tab[0] <= Tab[1]
    elif len(Tab) > 2:
        return test_tri(Tab[1:])


""" ###########################################################################
Un mot est un palindrome si on peut le lire dans les deux sans
de gauche à droite et de droite à gauche. Exemple KAYAK est un palindrome.
Ecrire une fonction récursive permettant de vérifier si un mot est palindrome.
"""

def test_pal(chaine):
    if len(chaine) <= 1:
        return True
    if chaine[0]==chaine[-1]:
        return test_pal(chaine[1:-1])
    else:
        return False


""" ###########################################################################
Soit un tableau d’’entiers contenant des valeurs 0 ou bien 1.
On appel composante connexe une suite contigue de nombres égaux à 1.
On voudrait changer la valeur de chaque composante connexe
de telle sorte que la première composante ai la valeur 2
la deuxième ai la valeur 3, la 3ème ait la valeur 4 et ainsi de suite.
Réaliser deux fonctions :

    1) La première fonction n’est pas récursive et
       a pour rôle de chercher la position d’un 1 dans un tableau.
    2) La deuxième fonction est récursive.
       Elle reçoit la position d’un 1 dans une séquence
       et propage une valeur x à toutes les valeur 1 de la composante connexe.
"""
