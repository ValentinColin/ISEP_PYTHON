import matplotlib.pyplot as plt
from numpy import pi,log

# nombre de terme à stocké
N = 9000

### conjecture [3x+1]
def syra1(u0,first=False):
    """Itérateur sur les termes de la suite de syracuse
    commence à u0 et fini à 1"""
    if first:
        yield u0
    while u0 > 1:
        if u0%2 == 0:
            u0//=2
            yield u0
        else:
            u0 = 3*u0+1
            yield u0

### conjecture [(3x+1)/2]
def syra2(u0,first=False):
    """Itérateur sur les termes de la suite de syracuse
    commence à u0 et fini à 1"""
    if first:
        yield u0
    while u0 > 1:
        if u0%2 == 0:
            u0//=2
            yield u0
        else:
            u0 = (3*u0+1)//2
            yield u0

def syra3(u0,first=False):
    """Itérateur sur les termes de la suite de syracuse
    commence à u0 et fini à 1"""
    if first:
        yield u0
    while u0 > 1:
        if u0%2 == 0:
            u0//=2
            yield u0
        else:
            u0 = 5*u0+1
            yield u0

def tempsVol(u0):
    return len(list(syra(u0)))

def tempsVolAlt(u0):
    n=0
    for u in syra(u0):
        n+=1
        if u <= u0:
            break
    return n-1

def altMax(u0):
    max = u0
    for u in syra(u0):
        if u > max:
            max = u
    return max

################################## Partie 1 ##################################
"""
syra = syra1

indice = list(range(1,N+1))
temps_de_vol = [tempsVol(u0+1) for u0 in range(N)]
temps_de_vol_en_altitude = [tempsVolAlt(u0+1) for u0 in range(N)]
altitude_max = [altMax(u0+1) for u0 in range(N)]

# dictionnaire qui stock pour chaque u0 (1 à 9000) leurs (tpsVol,tpsVolAlt,altMax)
stock = dict((n+1,(temps_de_vol[n],temps_de_vol_en_altitude[n],altitude_max[n])) for n in range(N))
# print(stock)

# Afficher le temps de vol pour les 100 premiers entiers
#for n in range(100):
    #print("temps de vol de {}:".format(n+1),stock[n+1][0])

# Altitude maximale atteinte par toute la séquence
max_alt = 1
max_tps_alt = 0
for _,tps_Alt,alt_Max in stock.values():
    if alt_Max > max_alt:
        max_alt = alt_Max
    if tps_Alt > max_tps_alt:
        max_tps_alt = tps_Alt

# print("l'altitude maximale de toute la séquence est "+str(max_alt))
# 8153620 pour les 9000 premières suites
# print("Le temps de vol en altitude maximale dans toute la séquence est "+str(max_tps_alt))
# 131 pour les 9000 premières suites
"""
################### Affichage graphique 1 ##################
"""
# Nuage de points du temps de vol
plt.subplot(321)
plt.title("graphique 1")
plt.plot(indice, temps_de_vol,".",markersize=2)

# Nuage de points du temps de vol en altitude
plt.subplot(323)
plt.plot(indice, temps_de_vol_en_altitude,".",markersize=2)

# Nuage de points de l'altitude maximale
plt.subplot(325)
plt.plot(indice, altitude_max,".",markersize=2)
plt.ylim(0,100000)

# plt.show()
"""
################################## Partie 2 ##################################
"""
syra = syra2

indice = list(range(1,N+1))
temps_de_vol = [tempsVol(u0+1) for u0 in range(N)]
temps_de_vol_en_altitude = [tempsVolAlt(u0+1) for u0 in range(N)]
altitude_max = [altMax(u0+1) for u0 in range(N)]

# dictionnaire qui stock pour chaque u0 (1 à 9000) leurs (tpsVol,tpsVolAlt,altMax)
stock = dict((n+1,(temps_de_vol[n],temps_de_vol_en_altitude[n],altitude_max[n])) for n in range(N))
# print(stock)

# Afficher le temps de vol pour les 100 premiers entiers
#for n in range(100):
    #print("temps de vol de {}:".format(n+1),stock[n+1][0])

# Altitude maximale atteinte par toute la séquence
max_alt = 1
max_tps_alt = 0
for _,tpsAlt,altMax in stock.values():
    if altMax > max_alt:
        max_alt = altMax
    if tpsAlt > max_tps_alt:
        max_tps_alt = tpsAlt

# print("l'altitude maximale de toute la séquence est "+str(max_alt))
# 4076810 pour les 9000 premières suites
# print("Le temps de vol en altitude maximale dans toute la séquence est "+str(max_tps_alt))
# 80 pour les 9000 premières suites
"""
############################ Affichage graphique 2 ############################
"""
# Nuage de points du temps de vol
plt.subplot(322)
plt.title("graphique 2")
plt.plot(indice, temps_de_vol,".",markersize=2)

# Nuage de points du temps de vol en altitude
plt.subplot(324)
plt.plot(indice, temps_de_vol_en_altitude,".",markersize=2)

# Nuage de points de l'altitude maximale
plt.subplot(326)
plt.plot(indice, altitude_max,".",markersize=2)
plt.ylim(0,100000)

plt.show()
"""
############################ Affichage graphique 3 ############################
"""
# Spirale logarithmique
P = 256
theta = [2*pi*log(n)/log(2) for n in range(1,P+1)]
r = list(range(1,P+1))

theta_bleu = [2*pi*log(n)/log(2) for n in range(0,P+1,2)]
r_bleu = [n//2 for n in range(0,P+1,2)]

theta_rouge = [2*pi*log(n)/log(2) for n in range(1,P+2,2)]
r_rouge = [(3*n+1)//2 for n in range(1,P+2,2)]

plt.polar(theta      ,r      ,'.',markersize=2,color="k")
plt.polar(theta_bleu ,r_bleu ,'-',markersize=2,color="b")
plt.polar(theta_rouge,r_rouge,'-',markersize=2,color="r")

plt.show()
"""
################################## Partie 3 ##################################

syra = syra3

for k in range(4):
    print("suite:",list(syra(k+1,True)),"temps de vol:",tempsVol(k+1))
z=0
for u in syra(5):
    z+=1
    print(u)
    if z>20:
        break

"""
indice = list(range(1,N+1))
temps_de_vol = [tempsVol(u0+1) for u0 in range(N)]
temps_de_vol_en_altitude = [tempsVolAlt(u0+1) for u0 in range(N)]
altitude_max = [altMax(u0+1) for u0 in range(N)]

# dictionnaire qui stock pour chaque u0 (1 à 9000) leurs (tpsVol,tpsVolAlt,altMax)
stock = dict((n+1,(temps_de_vol[n],temps_de_vol_en_altitude[n],altitude_max[n])) for n in range(N))
# print(stock)

# Afficher le temps de vol pour les 100 premiers entiers
#for n in range(100):
    #print("temps de vol de {}:".format(n+1),stock[n+1][0])

# Altitude maximale atteinte par toute la séquence
max_alt = 1
max_tps_alt = 0
for _,tpsAlt,altMax in stock.values():
    if altMax > max_alt:
        max_alt = altMax
    if tpsAlt > max_tps_alt:
        max_tps_alt = tpsAlt

# print("l'altitude maximale de toute la séquence est "+str(max_alt))
#  pour les 9000 premières suites
# print("Le temps de vol en altitude maximale dans toute la séquence est "+str(max_tps_alt))
#  pour les 9000 premières suites
"""
############################ Affichage graphique 3 ############################
"""
# Nuage de points du temps de vol
plt.subplot(311)
plt.title("graphique 3")
plt.plot(indice, temps_de_vol,".",markersize=2)

# Nuage de points du temps de vol en altitude
plt.subplot(312)
plt.plot(indice, temps_de_vol_en_altitude,".",markersize=2)

# Nuage de points de l'altitude maximale
plt.subplot(312)
plt.plot(indice, altitude_max,".",markersize=2)
plt.ylim(0,100000)

plt.show()
"""
