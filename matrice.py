"""
################################################################################
#
#                            FONCTION MATRICIELLE
#
#    Créateurs : Valentin  COLIN
#
#    Version : 2019
#
###############################################################################
#
#                                  SOMMAIRE
#
#    1.  tailleMatrice (matrice)   .................................. ligne  37
#    2.  typeMatrice (matrice)   .................................... ligne  52
#    3.  estTypeTrigInf (matrice,ligne)   ........................... ligne  72
#    4.  estTypeTrigSup (matrice,ligne)   ........................... ligne  88
#    5.  estTypeDiag (matrice,ligne)   .............................. ligne 104
#    6.  estTypeNulle (matrice,ligne,colonne)   ..................... ligne 120
#    7.  addType (type,add)   ....................................... ligne 132
#    8.  creeMatriceFull (ligne,colonne,scalaire)   ................. ligne 137
#    9.  creeMatriceId (ordre)   .................................... ligne 146
#   10.  addition (matriceA,matriceB)   ............................. ligne 153
#   11.  produitScal (scalaire,matrice)   ........................... ligne 166
#   12.  produitSimple (matriceA,matriceB)   ........................ ligne 174
#   13.  puissancesSimple (matrice,puissance)   ..................... ligne 187
#   14.  produitMat (matriceA,matriceB)   ........................... ligne 196
#   15.  puissancesMat (matrice,puissance)   ........................ ligne 214
#   16.  transposer (matrice)   ..................................... ligne 229
#
###############################################################################
"""
# --coding:utf-8--

from copy import deepcopy

def tailleMatrice(matrice):
    """Détermine la taille de la matrice sous la forme d'un t-uples
    n ligne et p colonne (n,p)
    si cette matrice est incomplète (ligne de taille différente) renvoie None"""
    n=len(matrice)
    p=len(matrice[0]) # longueur de la première ligne
    resultat=True
    for ligne in matrice:
        if len(ligne) != p: # si chaque ligne est de la même longueur que la première
            resultat=False
    if resultat==True:
        return (n,p)
    else:
        return None

def typeMatrice(matrice):
    """Détermine le type de matrice: VIDE/NULLE/CARRE/DIAG/TRIG_INF/TRIG_SUP
    sachant que DIAG => TRIG => CARRE"""
    n,p=tailleMatrice(matrice)
    type=None
    if n*p == 0: # si au moins l'un des deux est nul
        type=addType(type,add="VIDE")
    else:
        if estTypeNulle(matrice,n,p):
            type=addType(type,add="NULLE")
        if n==p:
            type=addType(type,add="CARRE")
            if estTypeTrigInf(matrice,n):
                type=addType(type,add="TRIG_INF")
            if estTypeTrigSup(matrice,n):
                type=addType(type,add="TRIG_SUP")
            if ("TRIG_INF" in type) and ("TRIG_SUP" in type):
                type=addType(type,add="DIAG")
    return type

def estTypeTrigInf(matrice,ligne):
    """détermine si une matrice carré de taille n: est triangulaire inférieur"""
    FullZero=True
    for i in range(ligne):
        for j in range(ligne):
            if i<j:
                if not matrice[i][j]==0:
                    FullZero=False
                    break
        if not FullZero:
            break
    if FullZero:
        return True
    else:
        return False

def estTypeTrigSup(matrice,ligne):
    """détermine si une matrice carré de taille n: est triangulaire supérieur"""
    FullZero=True
    for i in range(ligne):
        for j in range(ligne):
            if i>j:
                if not matrice[i][j]==0:
                    FullZero=False
                    break
        if not FullZero:
            break
    if FullZero:
        return True
    else:
        return False

def estTypeDiag(matrice,ligne):
    """détermine si une matrice carré de taille n: est diagonale"""
    FullZero=True
    for i in range(ligne):
        for j in range(ligne):
            if i!=j:
                if not matrice[i][j]==0:
                    FullZero=False
                    break
        if not FullZero:
            break
    if FullZero:
        return True
    else:
        return False

def estTypeNulle(matrice,ligne,colonne):
    """Détermine si une matrice est nulle"""
    FullZero=True
    for i,j in ((k,l) for k in range(ligne) for l in range(colonne)):
        if not matrice[i][j]==0:
            FullZero=False
            break
    if FullZero:
        return True
    else:
        return False

def addType(type,add):
    """fusionne les type et add en les séparant d'un séparateur  |         ."""
    if type==None: return add
    else:          return type+" | "+add

def creeMatriceFull(ligne,colonne,scalaire):
    """crée une matrice remplie du même scalaire de taille (n,p)"""
    matrice=[]
    for i in range(ligne):
        matrice.append([])
        for j in range(colonne):
            matrice[i].append(scalaire)
    return matrice

def creeMatriceId(ordre):
    """crée une matrice identité de taille n"""
    ID=creeMatriceFull(ordre,ordre,0)
    for i in range(ordre):
        ID[i][i]=1
    return ID

def addition(matriceA,matriceB):
    """ajoute la seconde matrice à la première matrice
    et renvoie donc la première matrice
    si elles ne sont pas de même taille renvoie None"""
    if tailleMatrice(matriceA)==tailleMatrice(matriceB):
        (n,p)=tailleMatrice(matriceA)
        for i in range(n):
            for j in range(p):
                matriceA[i][j]+=matriceB[i][j]
        return matriceA
    else:
        return None

def produitScal(matrice,scalaire):
    """Calcul le produit par un scalaire de la matrice"""
    (n,p)=tailleMatrice(matrice)
    for i in range(n):
        for j in range(p):
            matrice[i][j]*=scalaire
    return matrice

def produitSimple(matriceA,matriceB):
    """multiplie terme à terme la matriceA par la matriceB
    et renvoie la première matriceA (modifié)
    si elles ne sont pas de même taille renvoie None"""
    if tailleMatrice(matriceA)==tailleMatrice(matriceB):
        (n,p)=tailleMatrice(matriceA)
        for i in range(n):
            for j in range(p):
                matriceA[i][j]*=matriceB[i][j]
        return matriceA
    else:
        return None

def puissancesSimple(matrice,puissance):
    """Calcul la puissance d'une matrice en utilisant le produit terme à terme
    renvoie une autre matrice"""
    (n,p)=tailleMatrice(matrice)
    matriceP=creeMatriceFull(n,p,1)
    for _ in range(puissance):
        matriceP=produitSimple(matriceP,matrice)
    return matriceP

def produitMat(matriceA,matriceB):
    """argument: matriceA de taille (n,p)
                 matriceB de taille (p,m)
    calcule le produit matricielle de A par B
    et renvoie une nouvelle matrice
    renvoie None en cas d'erreur"""
    (n,p)=tailleMatrice(matriceA)
    (q,m)=tailleMatrice(matriceB)
    if p==q:
        matriceC=creeMatriceFull(n,m,0)
        for i in range(n):
            for j in range(m):
                for k in range(p):
                    matriceC[i][j]=matriceC[i][j]+matriceA[i][k]*matriceB[k][j]
        return matriceC
    else:
        return None

def puissancesMat(matrice,puissance):
    """Calcule la puissance d'une matrice en produit matricielle et non simple
    il est donc nécessaire d'avoir une matrice carré"""
    (n,p)=tailleMatrice(matrice)
    if n==p:
        matOrigine=deepcopy(matrice)
        #print("origine",matOrigine)
        #print("produitmat",produitMat(matrice,matOrigine))
        for _ in range(puissance-1):
            #print(matrice)
            matrice=produitMat(matrice,matOrigine)
        return matrice
    else:
        return None

def transposer(matrice):
    """Détermine la transposer de la matrice
    renvoie une nouvelle matrice transposer"""
    (n,p)=tailleMatrice(matrice)
    matriceT=creeMatriceFull(p,n,0)
    for i in range(n):
        for j in range(p):
            matriceT[j][i]=matrice[i][j]
    return matriceT
