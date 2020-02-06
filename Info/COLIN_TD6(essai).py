# Valentin Colin
#--conding:utf-8--
from PIL import Image
import numpy as np

################################## Fonctions ##################################
############### Manipulation de base
def rot_pi(tab): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après rotation de 180 degrés de l'image."""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            tab_r[-i-1][-j-1] = tab[i][j]
    return tab_r


def rot_d(tab): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après rotation de -90 degrés de l'image."""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((colonnes, lignes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            tab_r[j][-(i+1)] = tab[i][j]
    return tab_r


def rot_g(tab): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après rotation de +90 degrés de l'image."""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((colonnes, lignes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            tab_r[-(j+1)][i] = tab[i][j]
    return tab_r


def sym_h(tab): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après symétrie horizontale de l'image."""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)
    for i in range(lignes):
        tab_r[-(i+1)] = tab[i]
    return tab_r


def sym_v(tab): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après symétrie verticale de l'image."""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            tab_r[i][-(j+1)] = tab[i][j]
    return tab_r


############### Filtrage simple
def inversion(tab): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après l'inversion des niveau de gris
    de l'image. (ie. complément à 255 des niveau de gris)"""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            tab_r[i][j] = 255 - tab[i][j]
    return tab_r


def seuil(tab,valeur_seuil=122,valeur_basse=50,valeur_haute=190): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels ayant 2 valeur possible,
    la valeur basse et la valeur haute, décider en fonction
    de la position relative du niveau de gris face à une valeur seuil. """
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            if tab[i][j] <= valeur_seuil:
                tab_r[i][j] = valeur_basse
            else:
                tab_r[i][j] = valeur_haute
    return tab_r


def val_abs(tab,ecart=127): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels où la valeur devient: x <-- |x-ecart|."""
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)
    for i in range(lignes):
        for j in range(colonnes):
            tab_r[i][j] = abs(tab[i][j] - ecart)
    return tab_r


############### Filtrages plus évolués
filtre_simple = [1,1,1,
                 1,1,1,
                 1,1,1,1]

filtre_important = [1,1,1,1,1,
                    1,1,1,1,1,
                    1,1,1,1,1,
                    1,1,1,1,1,
                    1,1,1,1,1,2]

filtre_contours = [-1,-1,-1,
                   -1, 8,-1,
                   -1,-1,-1,1]

def filtrage(tab,filtre,S=None): # ok
    """À partir d'un tableau de pixel en niveau de gris donné:
    Renvoie un tableau de pixels après avoir appliquer un filtre sur l'image.
    Un filtre étant une liste de n^2+1 termes dont les n^2 premiers
    sont des coefficient appliquer à des certains pixels.
    Le dernier terme indique la taille du filtre dans le sens de la distance
    Exemple: filtre = [1,1,1,
                       1,1,1,
                       1,1,1, 1]
    ou
             filtre = [1,1,1,1,1,
                       1,1,1,1,1,
                       1,1,1,1,1,
                       1,1,1,1,1,
                       1,1,1,1,1, 2]
                       """
    taille = tab.shape # (lignes, colonnes, profondeur)
    lignes, colonnes = taille[0], taille[1]
    tab_r = np.zeros((lignes, colonnes), dtype=np.uint8)

    T = filtre[-1] # écart max au pixel central dans le filtre
    if S is None:
        S = sum(filtre[:-1])

    for i in range(T,lignes-T):
        for j in range(T,colonnes-T):
            # liste des valeurs des pixels dans le sens de lecture
            pixels = [tab[i+a][j+b] for a in range(-T,T+1) for b in range(-T,T+1)]
            # calcul de la valeur du pixel central
            tab_r[i][j] = int(sum(map(lambda x,y: x*y,pixels,filtre[:-1]))/S)

    return tab_r

###############################################################################

im = Image.open("/Users/valentin/Desktop/seba.tiff")
a, b = im.size          # colonnes, lignes
t_im = np.array(im)     # Tableau des valeurs originale

#   Copie couleurs
# t_mod = np.copy(t_im)

#   Copie de la première composante car image en noir et blanc
t_mod = np.array([[t_im[i][j][0] for j in range(a)] for i in range(b)])
## Ou pour les conversion en gris des images en couleurs
# conv_gris = lambda p: int(0.299*p[0]+0.587*p[1]+0.114*p[2])
# t_mod = np.array([[conv_gris(list(t_im[i][j])) for j in range(a)] for i in range(b)])

taille = t_mod.shape    # taille du tableau (peut être à 2 ou 3 dimensions)


# IMAGE ORIGINALE
# pour crée une image à partir d'un tableau numpy
im2 = Image.fromarray(t_mod)
# pour afficher directement l'image (si possible)
im2.show(title="Image_originale")

# pour sauvgarder l'image
# im2.save("/Users/valentin/Desktop/seba_mod.tiff")

############ Tests des fonctions de traitement d'images

# im2 = Image.fromarray(rot_pi(t_mod))
# im2.show(title="Rotation_pi")

# im2 = Image.fromarray(rot_d(t_mod))
# im2.show(title="Rotation_droite")

# im2 = Image.fromarray(rot_g(t_mod))
# im2.show(title="Rotation_gauche")

# im2 = Image.fromarray(sym_h(t_mod))
# im2.show(title=""Symétrie_horizontale)

# im2 = Image.fromarray(sym_v(t_mod))
# im2.show(title="Symétrie_verticale")

# im2 = Image.fromarray(inversion(t_mod))
# im2.show(title="Inversion")

# im2 = Image.fromarray(seuil(t_mod))
# im2.show(title="Seuil")

# im2 = Image.fromarray(val_abs(t_mod))
# im2.show(title="Rapprochement_des_extrêmes")

# im2 = Image.fromarray(filtrage(t_mod,filtre_simple))
# im2.show(title="Filtre_simple")

# im2 = Image.fromarray(filtrage(t_mod,filtre_important))
# im2.show(title="Filtre_important")

# im2 = Image.fromarray(filtrage(t_mod,filtre_contours,S=1))
# im2.show(title="Renforcement_des_contours")
