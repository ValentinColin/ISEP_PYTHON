"""
###############################################################################
#
#                    TD2: quaternions, octonions, sédénions
#
#    Créateur(s) : Valentin COLIN
#
#    Version : 2019
#
###############################################################################
#
#                                  CLASSE(S)
#
#    1.    Ha:  .................................................... ligne  112
#    1.1   ------> __init__  ....................................... ligne  117
#    1.2   ------> tupleh  ......................................... ligne  125
#    1.3   ------> __repr__  ....................................... ligne  130
#    1.4   ------> __add__  ........................................ ligne  141
#    1.5   ------> __sub__  ........................................ ligne  147
#    1.6   ------> __eq__  ......................................... ligne  153
#    1.7   ------> __neq__  ........................................ ligne  157
#    1.8   ------> __neg__  ........................................ ligne  161
#    1.9   ------> conjh  .......................................... ligne  166
#    1.10  ------> __mul__  ........................................ ligne  171
#    1.11  ------> __pow__  ........................................ ligne  179
#    1.12  ------> __rmul__  ....................................... ligne  187
#    1.13  ------> __abs__  ........................................ ligne  192
#    1.14  ------> invh  ........................................... ligne  196
#    1.15  ------> __truediv__  .................................... ligne  200
#    1.16  ------> carreh  ......................................... ligne  204
#    1.17  ------> rot  ............................................ ligne  208
#
#    2.    Oc(Ha):  ................................................ ligne  219
#    2.1   ------> __init__  ....................................... ligne  224
#    2.2   ------> tupleoc  ........................................ ligne  232
#    2.3   ------> __repr__  ....................................... ligne  237
#    2.4   ------> __add__  ........................................ ligne  248
#    2.5   ------> __sub__  ........................................ ligne  256
#    2.6   ------> __eq__  ......................................... ligne  264
#    2.7   ------> __neq__  ........................................ ligne  268
#    2.8   ------> __neg__  ........................................ ligne  272
#    2.9   ------> conjoc  ......................................... ligne  278
#    2.10  ------> __mul__  ........................................ ligne  284
#    2.11  ------> __pow__  ........................................ ligne  292
#    2.12  ------> __rmul__  ....................................... ligne  301
#    2.13  ------> __abs__  ........................................ ligne  306
#    2.14  ------> invoc  .......................................... ligne  310
#    2.15  ------> __truediv__  .................................... ligne  314
#    2.16  ------> carreoc  ........................................ ligne  318
#
#    3.    Se(Oc):  ................................................ ligne  323
#    3.1   ------> __init__  ....................................... ligne  328
#    3.2   ------> tuplese  ........................................ ligne  336
#    3.3   ------> __repr__  ....................................... ligne  341
#    3.4   ------> __add__  ........................................ ligne  352
#    3.5   ------> __sub__  ........................................ ligne  360
#    3.6   ------> __eq__  ......................................... ligne  368
#    3.7   ------> __neq__  ........................................ ligne  372
#    3.8   ------> __neg__  ........................................ ligne  376
#    3.9   ------> conjse  ......................................... ligne  382
#    3.10  ------> __mul__  ........................................ ligne  388
#    3.11  ------> __pow__  ........................................ ligne  396
#    3.12  ------> __rmul__  ....................................... ligne  406
#    3.13  ------> __abs__  ........................................ ligne  411
#    3.14  ------> invse  .......................................... ligne  415
#    3.15  ------> __truediv__  .................................... ligne  419
#    3.16  ------> carrese  ........................................ ligne  423
#
#    4.    Trigi(Se):  ............................................. ligne  428
#    4.1   ------> __init__  ....................................... ligne  433
#    4.2   ------> tupletrigi  ..................................... ligne  441
#    4.3   ------> __repr__  ....................................... ligne  446
#    4.4   ------> __add__  ........................................ ligne  457
#    4.5   ------> __sub__  ........................................ ligne  465
#    4.6   ------> __eq__  ......................................... ligne  473
#    4.7   ------> __neq__  ........................................ ligne  477
#    4.8   ------> __neg__  ........................................ ligne  481
#    4.9   ------> conjtrigi  ...................................... ligne  487
#    4.10  ------> __mul__  ........................................ ligne  493
#    4.11  ------> __pow__  ........................................ ligne  501
#    4.12  ------> __rmul__  ....................................... ligne  511
#    4.13  ------> __abs__  ........................................ ligne  516
#    4.14  ------> invtrigi  ....................................... ligne  520
#    4.15  ------> __truediv__  .................................... ligne  524
#    4.16  ------> carretrigi  ..................................... ligne  528
#
#    5.    Sexa(Trigi):  ........................................... ligne  533
#    5.1   ------> __init__  ....................................... ligne  538
#    5.2   ------> tuplesexa  ...................................... ligne  546
#    5.3   ------> __repr__  ....................................... ligne  551
#    5.4   ------> __add__  ........................................ ligne  562
#    5.5   ------> __sub__  ........................................ ligne  570
#    5.6   ------> __eq__  ......................................... ligne  578
#    5.7   ------> __neq__  ........................................ ligne  582
#    5.8   ------> __neg__  ........................................ ligne  586
#    5.9   ------> conjsexa  ....................................... ligne  592
#    5.10  ------> __mul__  ........................................ ligne  598
#    5.11  ------> __pow__  ........................................ ligne  606
#    5.12  ------> __rmul__  ....................................... ligne  616
#    5.13  ------> __abs__  ........................................ ligne  621
#    5.14  ------> invsexa  ........................................ ligne  625
#    5.15  ------> __truediv__  .................................... ligne  629
#    5.16  ------> carresexa  ...................................... ligne  633
#
###############################################################################
# --coding:utf-8--
"""
from math import sqrt,sin,cos,pi,radians



class Ha:
    """Classe des Quaternions."""

    dim = 4 # dimmension de l'espace

    def __init__(self,*coef):
        """Constructeur d'instances."""
        if len(coef) != Ha.dim:
            raise TypeError("{} coordonnates needed".format(Ha.dim))
        self.coef = list(coef)
        self.A = complex(*self.coef[:Ha.dim//2])
        self.B = complex(*self.coef[Ha.dim//2:])

    def tupleh(self):
        """Renvoie les éléments de self sous forme de tuples
        (i.e ses coordonnées)."""
        return tuple(self.coef)

    def __repr__(self):
        """renvoie une représentation de self en string."""
        sign = {}
        letter = ["","i","j","k"]
        for i in range(1,Ha.dim):
            sign[i] = ("+" if self.coef[i] >= 0 else "")
        text = str(self.coef[0])
        for k in range(1,Ha.dim):
            text += " {}{}{}".format(sign[k],self.coef[k],letter[k])
        return "("+text+")"

    def __add__(self,other):
        """Renvoie l'addition de self et other (self+other)."""
        zA = self.A + other.A
        zB = self.B + other.B
        return Ha(zA.real,zA.imag,zB.real,zB.imag)

    def __sub__(self,other):
        """Renvoie la soustraction de self et other (self-other)."""
        zA = self.A - other.A
        zB = self.B - other.B
        return Ha(zA.real,zA.imag,zB.real,zB.imag)

    def __eq__(self,other):
        """Test d'égalité entre self et other (self==other)."""
        return (self.A == other.A) and (self.B == other.B)

    def __neq__(self,other):
        """Test de non égalité entre self et other (self!=other)."""
        return (self.A != other.A) or (self.B != other.B)

    def __neg__(self):
        """Renvoie l'opposé de self (-self)."""
        coef = [-self.coef[i] for i in range(Ha.dim)]
        return Ha(*coef)

    def conjh(self):
        """Renvoie le quaternion conjugué de self."""
        coef = [self.coef[0]] + [-self.coef[i] for i in range(1,Ha.dim)]
        return Ha(*coef)

    def __mul__(self,other):
        """Renvoie le produit de self et other (self*other)."""
        A, B = self.A, self.B
        C, D = other.A, other.B
        E = A*C - D.conjugate()*B # complex
        F = D*A + B*C.conjugate() # complex
        return Ha(E.real,E.imag,F.real,F.imag)

    def __pow__(self,p):
        """renvoie la puissance p-ième de self (self**p)."""
        A, B = self.A, self.B
        P, Q = self.A, self.B
        for _ in range(p-1):
            P,Q = A*P - B*Q.conjugate(), A*Q + B*P.conjugate()
        return Ha(P.real,P.imag,Q.real,Q.imag)

    def __rmul__(self,r):
        """renvoie le produit de self par un scalaire (r*self)."""
        coef = [r*self.coef[i] for i in range(Ha.dim)]
        return Ha(*coef)

    def __abs__(self):
        """Renvoie le module de self (abs(self))."""
        return sqrt((self*self.conjh()).coef[0])

    def invh(self):
        """Renvoie l'inverse de self."""
        return (1/abs(self)**2) * self.conjh()

    def __truediv__(self,other):
        """Renvoie la division n de self par other (self/other)."""
        return self * other.invh()

    def carreh(self):
        """Renvoie le carré du module de self."""
        return sum([self.coef[i]**2 for i in range(Ha.dim)])

    def rot(self,other,alpha):
        """other (Ha) -> vecteur 3D représenter par un quaternion (0,x,y,z)
        alpha (radians) -> angle de rotation de self autour de other."""
        x, y, z = [other.coef[i] for i in range(1,Ha.dim)]
        q = Ha(cos(alpha/2), \
            sin(alpha/2)/abs(other) * x, \
            sin(alpha/2)/abs(other) * y, \
            sin(alpha/2)/abs(other) * z)
        return q * self * q.invh()


class Oc(Ha):
    """Classe des Octonions."""

    dim = 8 # dimmension de l'espace

    def __init__(self,*coef):
        """Constructeur d'instances."""
        if len(coef) != Oc.dim:
            raise TypeError("{} coordonnates needed".format(Oc.dim))
        self.coef = list(coef)
        self.A = Ha(*self.coef[:Oc.dim//2])
        self.B = Ha(*self.coef[Oc.dim//2:])

    def tupleoc(self):
        """Renvoie les éléments de self sous forme de tuples
        (i.e ses coordonnées)."""
        return tuple(self.coef)

    def __repr__(self):
        """renvoie une représentation de self en string."""
        sign = {}
        letter = ["","i","j","k","l","m","n","o"]
        for i in range(1,Oc.dim):
            sign[i] = ("+" if self.coef[i] >= 0 else "")
        text = str(self.coef[0])
        for k in range(1,Oc.dim):
            text += " {}{}{}".format(sign[k],self.coef[k],letter[k])
        return "("+text+")"

    def __add__(self,other):
        """Renvoie l'addition de self et other (self+other)."""
        H1 = self.A + other.A # quaternions
        H2 = self.B + other.B # quaternions
        coef1 = H1.tupleh()
        coef2 = H2.tupleh()
        return Oc(*coef1,*coef2)

    def __sub__(self,other):
        """Renvoie la soustraction de self et other (self-other)."""
        H1 = self.A - other.A # quaternions
        H2 = self.B - other.B # quaternions
        coef1 = H1.tupleh()
        coef2 = H2.tupleh()
        return Oc(*coef1,*coef2)

    def __eq__(self,other):
        """Test d'égalité entre self et other (self==other)."""
        return (self.A == other.A) and (self.B == other.B)

    def __neq__(self,other):
        """Test de non égalité entre self et other (self!=other)."""
        return (self.A != other.A) or (self.B != other.B)

    def __neg__(self):
        """Renvoie l'opposé de self (-self)."""
        O1 = (-self.A).tupleh() # quadruplet
        O2 = (-self.B).tupleh() # quadruplet
        return Oc(*O1,*O2)

    def conjoc(self):
        """Renvoie le quaternion conjugué de self."""
        O1 = (self.A.conjh()).tupleh() # quadruplet
        O2 = (-self.B).tupleh()        # quadruplet
        return Oc(*O1,*O2)

    def __mul__(self,other):
        """Renvoie le produit de self et other (self*other)."""
        A, B = self.A, self.B
        C, D = other.A, other.B
        E = A*C - D.conjh()*B # quaternions
        F = D*A + B*C.conjh() # quaternions
        return Oc(*E.tupleh(),*F.tupleh())

    def __pow__(self,p):
        """renvoie la puissance p-ième de self (self**p)."""
        A, B = self.A, self.B
        P, Q = self.A, self.B
        for _ in range(p-1):
            P,Q = A*P - B*Q.conjh(), A*Q + B*P.conjh()
        coef = [P.coef[i] for i in range(Ha.dim)]+[Q.coef[k] for k in range(Ha.dim)]
        return Oc(*coef)

    def __rmul__(self,r):
        """renvoie le produit de self par un scalaire (r*self)."""
        coef = [r*self.coef[i] for i in range(Oc.dim)]
        return Oc(*coef)

    def __abs__(self):
        """Renvoie le module de self (abs(self))."""
        return sqrt((self*self.conjoc()).coef[0])

    def invoc(self):
        """Renvoie l'inverse de self."""
        return (1/abs(self)**2) * self.conjoc()

    def __truediv__(self,other):
        """Renvoie la division n de self par other (self/other)."""
        return self * other.invoc()

    def carreoc(self):
        """Renvoie le carré du module de self."""
        return sum([self.coef[i]**2 for i in range(Oc.dim)])


class Se(Oc):
    """Classe des Sédénions"""

    dim = 16 # dimmension de l'espace

    def __init__(self,*coef):
        """Constructeur d'instances."""
        if len(coef) != Se.dim:
            raise TypeError("{} coordonnates needed".format(Se.dim))
        self.coef = list(coef)
        self.A = Oc(*self.coef[:Se.dim//2])
        self.B = Oc(*self.coef[Se.dim//2:])

    def tuplese(self):
        """Renvoie les éléments de self sous forme de tuples
        (i.e ses coordonnées)."""
        return tuple(self.coef)

    def __repr__(self):
        """renvoie une représentation de self en string."""
        sign = {}
        letter = ["e{}".format(i) for i in range(Se.dim)]
        for i in range(1,Se.dim):
            sign[i] = ("+" if self.coef[i] >= 0 else "")
        text = str(self.coef[0])
        for k in range(1,Se.dim):
            text += " {}{}{}".format(sign[k],self.coef[k],letter[k])
        return "("+text+")"

    def __add__(self,other):
        """Renvoie l'addition de self et other (self+other)."""
        O1 = self.A + other.A # octonions
        O2 = self.B + other.B # octonions
        coef1 = O1.tupleoc()
        coef2 = O2.tupleoc()
        return Se(*coef1,*coef2)

    def __sub__(self,other):
        """Renvoie la soustraction de self et other (self-other)."""
        O1 = self.A - other.A # octonions
        O2 = self.B - other.B # octonions
        coef1 = O1.tupleoc()
        coef2 = O2.tupleoc()
        return Se(*coef1,*coef2)

    def __eq__(self,other):
        """Test d'égalité entre self et other (self==other)."""
        return (self.A == other.A) and (self.B == other.B)

    def __neq__(self,other):
        """Test de non égalité entre self et other (self!=other)."""
        return (self.A != other.A) or (self.B != other.B)

    def __neg__(self):
        """Renvoie l'opposé de self (-self)."""
        O1 = (-self.A).tupleoc() # octuplet
        O2 = (-self.B).tupleoc() # octuplet
        return Se(*O1,*O2)

    def conjse(self):
        """Renvoie le quaternion conjugué de self."""
        O1 = (self.A.conjoc()).tupleoc() # octuplet
        O2 = (-self.B).tupleoc()         # octuplet
        return Se(*O1,*O2)

    def __mul__(self,other):
        """Renvoie le produit de self et other (self*other)."""
        A, B = self.A, self.B
        C, D = other.A, other.B
        E = A*C - D.conjoc()*B # octonions
        F = D*A + B*C.conjoc() # octonions
        return Se(*E.tupleoc(),*F.tupleoc())

    def __pow__(self,p):
        """renvoie la puissance p-ième de self (self**p)."""
        A, B = self.A, self.B
        P, Q = self.A, self.B
        for _ in range(p-1):
            P,Q = A*P - B*Q.conjoc(), A*Q + B*P.conjoc()
        coef1 = [P.coef[i] for i in range(Oc.dim)]
        coef2 = [Q.coef[k] for k in range(Oc.dim)]
        return Se(*coef1,*coef2)

    def __rmul__(self,r):
        """renvoie le produit de self par un scalaire (r*self)."""
        coef = [r*self.coef[i] for i in range(Se.dim)]
        return Se(*coef)

    def __abs__(self):
        """Renvoie le module de self (abs(self))."""
        return sqrt((self*self.conjse()).coef[0])

    def invse(self):
        """Renvoie l'inverse de self."""
        return (1/abs(self)**2) * self.conjse()

    def __truediv__(self,other):
        """Renvoie la division n de self par other (self/other)."""
        return self * other.invse()

    def carrese(self):
        """Renvoie le carré du module de self."""
        return sum([self.coef[i]**2 for i in range(Se.dim)])


class Trigi(Se):
    """Classe des Trigintaduonions."""

    dim = 32 # dimmension de l'espace

    def __init__(self,*coef):
        """Constructeur d'instances."""
        if len(coef) != Trigi.dim:
            raise TypeError("{} coordonnates needed".format(Trigi.dim))
        self.coef = list(coef)
        self.A = Se(*self.coef[:Trigi.dim//2])
        self.B = Se(*self.coef[Trigi.dim//2:])

    def tupletrigi(self):
        """Renvoie les éléments de self sous forme de tuples
        (i.e ses coordonnées)."""
        return tuple(self.coef)

    def __repr__(self):
        """renvoie une représentation de self en string."""
        sign = {}
        letter = ["e{}".format(i) for i in range(Trigi.dim)]
        for i in range(1,Trigi.dim):
            sign[i] = ("+" if self.coef[i] >= 0 else "")
        text = str(self.coef[0])
        for k in range(1,Trigi.dim):
            text += " {}{}{}".format(sign[k],self.coef[k],letter[k])
        return "("+text+")"

    def __add__(self,other):
        """Renvoie l'addition de self et other (self+other)."""
        s1 = self.A + other.A # sédénions
        s2 = self.B + other.B # sédénions
        coef1 = s1.tuplese()
        coef2 = s2.tuplese()
        return Trigi(*coef1,*coef2)

    def __sub__(self,other):
        """Renvoie la soustraction de self et other (self-other)."""
        s1 = self.A - other.A # sédénions
        s2 = self.B - other.B # sédénions
        coef1 = s1.tuplese()
        coef2 = s2.tuplese()
        return Trigi(*coef1,*coef2)

    def __eq__(self,other):
        """Test d'égalité entre self et other (self==other)."""
        return (self.A == other.A) and (self.B == other.B)

    def __neq__(self,other):
        """Test de non égalité entre self et other (self!=other)."""
        return (self.A != other.A) or (self.B != other.B)

    def __neg__(self):
        """Renvoie l'opposé de self (-self)."""
        s1 = (-self.A).tuplese() # 16-uplet
        s2 = (-self.B).tuplese() # 16-uplet
        return Trigi(*s1,*s2)

    def conjtrigi(self):
        """Renvoie le quaternion conjugué de self."""
        s1 = (self.A.conjse()).tuplese() # 16-uplet
        s2 = (-self.B).tuplese()         # 16-uplet
        return Trigi(*s1,*s2)

    def __mul__(self,other):
        """Renvoie le produit de self et other (self*other)."""
        A, B = self.A, self.B
        C, D = other.A, other.B
        E = A*C - D.conjse()*B # sédénions
        F = D*A + B*C.conjse() # sédénions
        return Trigi(*E.tuplese(),*F.tuplese())

    def __pow__(self,p):
        """renvoie la puissance p-ième de self (self**p)."""
        A, B = self.A, self.B
        P, Q = self.A, self.B
        for _ in range(p-1):
            P,Q = A*P - B*Q.conjse(), A*Q + B*P.conjse()
        coef1 = [P.coef[i] for i in range(Se.dim)]
        coef2 = [Q.coef[k] for k in range(Se.dim)]
        return Trigi(*coef1,*coef2)

    def __rmul__(self,r):
        """renvoie le produit de self par un scalaire (r*self)."""
        coef = [r*self.coef[i] for i in range(Trigi.dim)]
        return Trigi(*coef)

    def __abs__(self):
        """Renvoie le module de self (abs(self))."""
        return sqrt((self*self.conjtrigi()).coef[0])

    def invtrigi(self):
        """Renvoie l'inverse de self."""
        return (1/abs(self)**2) * self.conjtrigi()

    def __truediv__(self,other):
        """Renvoie la division n de self par other (self/other)."""
        return self * other.invtrigi()

    def carretrigi(self):
        """Renvoie le carré du module de self."""
        return sum([self.coef[i]**2 for i in range(Trigi.dim)])


class Sexa(Trigi):
    """Classe des Sexagintaquaternions."""

    dim = 64 # dimmension de l'espace

    def __init__(self,*coef):
        """Constructeur d'instances."""
        if len(coef) != Sexa.dim:
            raise TypeError("{} coordonnates needed".format(Sexa.dim))
        self.coef = list(coef)
        self.A = Trigi(*self.coef[:Sexa.dim//2])
        self.B = Trigi(*self.coef[Sexa.dim//2:])

    def tuplesexa(self):
        """Renvoie les éléments de self sous forme de tuples
        (i.e ses coordonnées)."""
        return tuple(self.coef)

    def __repr__(self):
        """renvoie une représentation de self en string."""
        sign = {}
        letter = ["e{}".format(i) for i in range(Sexa.dim)]
        for i in range(1,Sexa.dim):
            sign[i] = ("+" if self.coef[i] >= 0 else "")
        text = str(self.coef[0])
        for k in range(1,Sexa.dim):
            text += " {}{}{}".format(sign[k],self.coef[k],letter[k])
        return "("+text+")"

    def __add__(self,other):
        """Renvoie l'addition de self et other (self+other)."""
        t1 = self.A + other.A # Trigintaduonions
        t2 = self.B + other.B # Trigintaduonions
        coef1 = t1.tupletrigi()
        coef2 = t2.tupletrigi()
        return Sexa(*coef1,*coef2)

    def __sub__(self,other):
        """Renvoie la soustraction de self et other (self-other)."""
        t1 = self.A - other.A # Trigintaduonions
        t2 = self.B - other.B # Trigintaduonions
        coef1 = t1.tupletrigi()
        coef2 = t2.tupletrigi()
        return Sexa(*coef1,*coef2)

    def __eq__(self,other):
        """Test d'égalité entre self et other (self==other)."""
        return (self.A == other.A) and (self.B == other.B)

    def __neq__(self,other):
        """Test de non égalité entre self et other (self!=other)."""
        return (self.A != other.A) or (self.B != other.B)

    def __neg__(self):
        """Renvoie l'opposé de self (-self)."""
        t1 = (-self.A).tupletrigi() # 32-uplet
        t2 = (-self.B).tupletrigi() # 32-uplet
        return Sexa(*t1,*t2)

    def conjsexa(self):
        """Renvoie le quaternion conjugué de self."""
        t1 = (self.A.conjtrigi()).tupletrigi() # 32-uplet
        t2 = (-self.B).tupletrigi()         # 32-uplet
        return Sexa(*t1,*t2)

    def __mul__(self,other):
        """Renvoie le produit de self et other (self*other)."""
        A, B = self.A, self.B
        C, D = other.A, other.B
        E = A*C - D.conjtrigi()*B # Trigintaduonions
        F = D*A + B*C.conjtrigi() # Trigintaduonions
        return Sexa(*E.tupletrigi(),*F.tupletrigi())

    def __pow__(self,p):
        """renvoie la puissance p-ième de self (self**p)."""
        A, B = self.A, self.B
        P, Q = self.A, self.B
        for _ in range(p-1):
            P,Q = A*P - B*Q.conjtrigi(), A*Q + B*P.conjtrigi()
        coef1 = [P.coef[i] for i in range(Sexa.dim)]
        coef2 = [Q.coef[k] for k in range(Sexa.dim)]
        return Sexa(*coef1,*coef2)

    def __rmul__(self,r):
        """renvoie le produit de self par un scalaire (r*self)."""
        coef = [r*self.coef[i] for i in range(Sexa.dim)]
        return Sexa(*coef)

    def __abs__(self):
        """Renvoie le module de self (abs(self))."""
        return sqrt((self*self.conjsexa()).coef[0])

    def invsexa(self):
        """Renvoie l'inverse de self."""
        return (1/abs(self)**2) * self.conjsexa()

    def __truediv__(self,other):
        """Renvoie la division n de self par other (self/other)."""
        return self * other.invtrigi()

    def carresexa(self):
        """Renvoie le carré du module de self."""
        return sum([self.coef[i]**2 for i in range(Sexa.dim)])


if __name__=="__main__":
    ############################### QUATERNIONS ###############################
    i = Ha(0,1,0,0)
    j = Ha(0,0,1,0)
    # print("On vérifie la non commutativité:\nEst-ce que ij=k et ji=-k ?")
    # print("    i*j=",i*j,"\n    j*i=",j*i) # ok

    q1 = Ha(4, 1,0, 6)
    q2 = Ha(0, 6,1, 8)
    q3 = Ha(1,-1,7,-6)
    # print("On vérifie l'associativité:\nEst-ce que (q1.q2).q3 = q1.(q2.q3) ?")
    # print((q1*q2)*q3 == q1*(q2*q3))         # ok
    # print("\nModule de q3:      ",abs(q3))  # ok
    # print("Racine carré de 87:",sqrt(87))   # ok

    qv     = Ha(0,3,7,8)
    axeRot = Ha(0,1,1,1)
    angle = 120
    qvr = qv.rot(axeRot,radians(angle))
    # print("Rotation de qv={} par rapport à axeRot={} d'un angle de {} degrées".format(qv.tupleh(),axeRot.tupleh(),angle))
    # print("image:",qvr) # ok

    ################################ OCTONIONS ################################
    octo = Oc(6,7,-8,-5,0,3,5,-4)
    # print(octo.tupleoc()) # ok
    # print(octo) # ok

    j = Oc(0,0,1,0,0,0,0,0)
    n = Oc(0,0,0,0,0,0,1,0)
    # print("On vérifie la non commutativité:\nEst-ce que nj=l et jn=-l ?")
    # print("    n*j=",n*j,"\n    j*n=",j*n) # ok

    o1 = Oc(1,6,-9,-8,10,8, 0, 5)
    o2 = Oc(4,4, 4, 4, 3,3, 3,-3)
    o3 = Oc(1,9,-6,-3,-5,9,12, 4)
    # print("Vérifions l'associativité (o1.o2).o3 != o1.(o2.o3):")
    # print((o1*o2)*o3 != o1*(o2*o3)) # ok
    # print("\nModule de o3:       ",abs(o3))
    # print("Racine carré de 393:",sqrt(393)) # ok


    ################################ SÉDÉNIONS ################################
    sede = Se(6,7,-8,-5,0,3,5,-4,7,7,4,3,9,1,0,5)
    # print(sede.tuplese()) # ok
    # print(sede) # ok

    s1 = Se(0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1)
    s2 = Se(0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0)
    # print("On vérifie la non commutativité:\nEst-ce que s1.s2 != s2.s1 ?")
    # print("s1.s2 != s2.s1 ->",s1*s2 != s2*s1) # ok

    s1w = Se(1,6,-9,-8,10,8, 0, 5,0,0,0,0,0,0,0,1)
    s2q = Se(4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0)
    s3t = Se(1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0)
    # print("Vérifions l'associativité (s1.s2).s3 != s1.(s2.s3):")
    # print((s1w*s2q)*s3t != s1w*(s2q*s3t)) # ok
    # print("\nModule de s3t:      ",abs(s3t))
    # print("Racine carré de 394:",sqrt(394)) # ok

    ############################ Trigintaduonions #############################
    trigi = Trigi(6,7,-8,-5,0,3,5,-4,7,7,4,3,9,1,0,5,6,7,-8,-5,0,3,5,-4,7,7,4,3,9,1,0,5)
    # print(trigi.tupletrigi()) # ok
    # print(trigi) # ok

    t1 = Trigi(0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1)
    t2 = Trigi(0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0)
    # print("On vérifie la non commutativité:\nEst-ce que t1.t2 != t2.t1 ?")
    # print("t1.t2 != t2.t1 ->",t1*t2 != t2*t1)

    t1w = Trigi(1,6,-9,-8,10,8, 0, 5,0,0,0,0,0,0,0,1,1,6,-9,-8,10,8, 0, 5,0,0,0,0,0,0,0,1)
    t2q = Trigi(4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0,4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0)
    t3t = Trigi(1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0,1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0)
    # print("Vérifions l'associativité (t1w.t2q).t3t != t1w.(t2q.t3t):")
    # print((t1w*t2q)*t3t != t1w*(t2q*t3t))
    # print("\nModule de t3t:      ",abs(t3t))
    # print("Racine carré de 788:",sqrt(788))

    ########################## Sexagintaquaternions ###########################
    sexa = Sexa(6,7,-8,-5,0,3,5,-4,7,7,4,3,9,1,0,5,6,7,-8,-5,0,3,5,-4,7,7,4,3,9,1,0,5,\
    4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0,4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0)
    # print(sexa.tuplesexa()) # ok
    # print(sexa) # ok

    sx1 = Sexa(0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,\
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1)
    sx2 = Sexa(0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,\
    0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0)
    # print("On vérifie la non commutativité:\nEst-ce que sx1.sx2 != sx2.sx1 ?")
    # print("sx1.sx2 != sx2.sx1 ->",sx1*sx2 != sx2*sx1) # ok

    sx1 = Sexa(1,6,-9,-8,10,8, 0, 5,0,0,0,0,0,0,0,1,1,6,-9,-8,10,8, 0, 5,0,0,0,0,0,0,0,1,\
    4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0,4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0)
    sx2 = Sexa(4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0,4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0,\
    1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0,1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0)
    sx3 = Sexa(1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0,1,9,-6,-3,-5,9,12, 4,0,0,0,0,1,0,0,0,\
    0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0)
    # print("Vérifions l'associativité (sx1.sx2).sx3 != sx1.(sx2.sx3):")
    # print((sx1*sx2)*sx3 != sx1*(sx2*sx3)) # ok
    # print("\nModule de sx3:      ",abs(sx3)) # ok
    # print("Racine carré de 793:",sqrt(793))

    ############################# LOI DES CARRÉS ##############################
    ### testons la loi des Modules/carrés
    # quaternions
    h1 = Ha(7,4,2,9)
    h2 = Ha(1,7,4,5)
    h3 = h1*h2
    # print(h3.carreh() == h1.carreh() * h2.carreh()) # égalité correct

    # octonions
    o1 = Oc(3,5,7,9,0,3,1,6)
    o2 = Oc(1,2,3,4,9,8,7,6)
    o3 = o1*o2
    # print(o3.carreoc() == o1.carreoc() * o2.carreoc()) # égalité correct

    # sédénions
    s1l = Se(1,6,-9,-8,10,8, 0, 5,0,0,0,0,0,0,0,1)
    s2l = Se(4,4, 4, 4, 3,3, 3,-3,0,1,0,0,0,0,0,0)
    s3l = s1l*s2l
    # print(s3l.carrese() == s1l.carrese() * s2l.carrese()) # égalité incorrect
    ######
    # La loi des modules/carrés est FAUSSE pour les Sédénions
    ######
