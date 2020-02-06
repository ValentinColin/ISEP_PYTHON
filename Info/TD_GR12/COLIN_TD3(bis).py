from math import cos,atan,exp
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy import integrate
from scipy.special import jn



f = lambda x: cos(x) * (x-2)**2 * atan(x) * exp(-0.5*x)


fig = plt.figure()
plt.title("Fonction f")
X = np.linspace(0,30,1000)
Y = [f(x) for x in X]

plt.plot(X,Y)

plt.show()
