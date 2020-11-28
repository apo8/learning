import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)

x = np.arange(-5,5,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-1.1,6)
plt.show()