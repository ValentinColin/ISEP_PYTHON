import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt



porte  = lambda x: 1 if -0.5<x<0.5 else 0

plt.figure(figsize=(10,7))

Ns = [512,1024,2048,4096]

for N in Ns:

    x = np.linspace(-8.0, 8.0, N)
    y = np.array([*map(porte,x)])

    yf = fft(y)
    xf = np.linspace(-8.0, 8.0, N/2)

    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.suptitle('Spectre de la fonction pour différentes valeurs de N')
plt.legend(['N = {}'.format(N) for N in Ns])
plt.grid()
plt.show()
