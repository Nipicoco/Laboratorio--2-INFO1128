import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


t  = np.linspace(0,5,100) # 100 puntos entre 0 y 5
x  = t +np.random.normal(size=100) # 100 puntos aleatorios


#Deleting the linear trend along the data axis with the detrend function of the signal module
detrender = signal.detrend(x)


# Una tupla de la figura y la trama usando la función subplots de matplotlib y la función figure de matplotlib y figzise para definir el tamaño de la figura
#figsize en este caso es una tupla de 10, 5 que define el tamaño de la figura
plot = plt.figure(figsize=(10,3)), plt.plot(t,x,label='Tendency'), plt.plot(t,detrender,label='No Tendency'), plt.legend(), plt.grid(), plt.show()

