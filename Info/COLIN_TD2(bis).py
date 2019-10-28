#    COLIN Valentin

################################# Exercice 1 #################################

string = "LE FAIT QUE DE TOUTE SUITE REELLE BORNEE ON PEUT EXTRAIRE UNE SOUS\
SUITE CONVERGENTE CONSTITUE LE THEOREME DE BOLZANO ET WEIERSTRASS"

def enum(string):
    """Return a dict with the caract in key
    and the occurence of it in the string."""
    dict = {}
    for caract in string:
        if caract in dict:
            dict[caract] += 1
        else:
            dict[caract] = 1
    return dict

# print(enum(string))
enum_list = list(enum(string).items())
enum_list.sort(key=lambda tuple: tuple[1],reverse=True)
enum_list = [enum_list[i][0] for i in range(len(enum_list))]
# print(enum_list) # liste ordonnée suivant un ordre décroissant de fréquence d'appartion

################################# Exercice 2 #################################



################################# Exercice 3 #################################

class Polynome:

    def __init__(self,*coef):
        if isinstance(coef[0],(list,tuple)):
            coef = list(coef[0])
        self.coef = coef

        while self.coef[-1] == 0:  # on supprime les zéros inutiles
            del self.coef[-1]

    def deg(self):
        """Renvoie le degré du polynome."""
        if self.coef != [0]:
            return len(self.coef)-1
        else:
            return float('-inf')

    def __add__(self,other):
        """Renvoie l'addition des polynomes self et other (self+other)."""
        max_deg  = max(self.deg(),other.deg())
        return Polynome([self[i]+other[i] for i in range(max_deg)])

    def __mul__(self,other):
        """Renvoie le produit des polynomes self et other (self*other)."""
        r_deg  = self.deg() + other.deg() # degré du produit
        r_coef = [sum([self[i]*other[j] for i in range(k+1) for j in range(k+1) if i+j==k]) for k in range(r_deg+1)]
        return Polynome(*r_coef)

    def __pow__(self,p):
        """Renvoie la puissance p-ième (p est un entier naturel)
         du polynome self (self**p)."""
        result = 1
        if p > 0:
            result = self
            for _ in range(p-1):
                result = result*self
        return result

    def __str__(self):
        sign = {}
        for i in range(self.deg()+1):
            sign[i] = ("+" if self.coef[i] >= 0 else "")

        text = str(self.coef[0]) + " {} {}X".format(sign[1],self.coef[1])
        for k in range(2,self.deg()+1):
            text += " {} {}X**{}".format(sign[k],self.coef[k],k)
        return "("+text+")"
    __repr__=__str__

    def __call__(self,x):
        result = 0
        for k in range(len(self.coef)):
            result += self.coef[k] * x**k
        return result

    def __getitem__(self, key):
        """Return the coef of the polynomial."""
        try:
            return self.coef[key]
        except IndexError:
            if key >= 0:    return 0
            else:           raise IndexError

    def __setitem__(self, key, value):
        """"""
        while True:
            try:
                self.coef[key] = value
                break
            except IndexError:
                self.coef.append(0)


if __name__ == '__main__':
    P = Polynome(4,-3,2)
    Q = Polynome(-6,-1,7,5)
    print(P,Q)
    print(P*Q)
