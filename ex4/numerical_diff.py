import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2 + 0.1 * x

def function_2(x):
    return x[0]**2 + x[1]**2

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x - h)) / (2 * h)

def tangent_line(f,x):
    d = numerical_diff(f,x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

x = np.arange(0.0,20.0,0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1,5)
y2 = tf(x)

plt.plot(x,y)
plt.plot(x,y2)
plt.show()
