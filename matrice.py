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
#                       (NOTE: commenter le script)
#
#    0.  tailleMatrice (matrice)   .................................. ligne  37
#    1.  typeMatrice (matrice)   .................................... ligne  52
#    2.  estTypeTrigInf (matrice,ligne)   ........................... ligne  72
#    3.  estTypeTrigSup (matrice,ligne)   ........................... ligne  88
#    4.  estTypeDiag (matrice,ligne)   .............................. ligne 104
#    5.  estTypeNulle (matrice,ligne,colonne)   ..................... ligne 120
#    6.  addType (type,add)   ....................................... ligne 132
#    7.  creeMatriceNulle (ligne,colonne)   ......................... ligne 137
#    8.  creeMatriceId (ordre)   .................................... ligne 146
#    9.  addition (matriceA,matriceB)   ............................. ligne 153
#   10.  produitSimple(matriceA,matriceB)   ......................... ligne 166
#   11.  produitMat(matriceA,matriceB)   ............................ ligne 179
#   12.  transposer (matrice)   ..................................... ligne 197
#
###############################################################################
"""
# --coding:utf-8--




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

def creeMatriceNulle(ligne,colonne):
    """crée une matrice nulle de taille (n,p)"""
    matrice=[]
    for i in range(ligne):
        matrice.append([])
        for j in range(colonne):
            matrice[i].append(0)
    return matrice

def creeMatriceId(ordre):
    """crée une matrice identité de taille n"""
    ID=creeMatriceNulle(ordre,ordre)
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

def produitSimple(matriceA,matriceB):
    """multiplie la matriceA par la matriceB
    et renvoie donc la première matriceA
    si elles ne sont pas de même taille renvoie None"""
    if tailleMatrice(matriceA)==tailleMatrice(matriceB):
        (n,p)=tailleMatrice(matriceA)
        for i in range(n):
            for j in range(p):
                matriceA[i][j]*=matriceB[i][j]
        return matriceA
    else:
        return None

def produitMat(matriceA,matriceB):
    """argument: matriceA de taille (n,p)
                 matriceB de taille (p,m)
    calcule le produit matricielle de A par B
    et renvoie une nouvelle matrice
    renvoie None en cas d'erreur"""
    (n,p)=tailleMatrice(matriceA)
    (q,m)=tailleMatrice(matriceB)
    if p==q:
        matriceC=creeMatriceNulle(n,m)
        for i in range(n):
            for j in range(m):
                for k in range(p):
                    matriceC[i][j]=matriceC[i][j]+matriceA[i][k]*matriceB[k][j]
        return matriceC
    else:
        return None

def transposer(matrice):
    """Détermine la transposer de la matrice
    renvoie une nouvelle matrice transposer"""
    (n,p)=tailleMatrice(matrice)
    matriceT=creeMatriceNulle(p,n)
    for i in range(n):
        for j in range(p):
            matriceT[j][i]=matrice[i][j]
    return matriceT
