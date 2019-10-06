# --coding:utf-8--
def tri(listeNT=[]):
    """prend une liste de nombre ENTIER en argument et renvoie la liste triée"""
    for elem in listeNT:
        if not isinstance(elem,(int,float)):
            print("TypeError: la liste donner en arguments n'est pas une liste de nombre")
            raise ValueError
            # return listeNT #renvoie la liste non modifié en cas d'erreur
    listeT=[]
    for k in range(len(listeNT)): # je fais len(listeNT) boucle pour retirer le plus petit à chaque fois
        min=listeNT[0]
        for elem in listeNT:# je parcours les elem restant
            if elem<=min:   # pour voir si je trouve un nombre encore plus petit
                min=elem
        listeT.append(min)
        del listeNT[listeNT.index(min)]
    return listeT # renvoie la liste trier
