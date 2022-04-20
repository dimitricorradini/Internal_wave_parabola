import numpy as np
import matplotlib.pyplot as plt


x = np.zeros((50000,))
y = np.zeros((50000,))
x_true = []
y_true = []
y[0]= 0
c = 1
a = 0.48
print(a)
b=np.random.uniform(-1, 1)
print(b)
x[0]= -b/a
for i in range(1, 50000):


    if (y[i-1] > 1-(a*a)/4):
        c *=-1
    x[i] = 1/2*(-a+c*np.sqrt(a*a-4*(b-1)))
    y[i] = 1-x[i]*x[i]
    
    if (y[i]<0):
        c*=-1
        y[i] = 0
        x[i] = -b/a
    if (i>30000):
        x_true.append(x[i])
        y_true.append(y[i])
    a*=-1
    c*=-1
    b = a*(-x[i])+y[i]

plt.plot(x_true, y_true, linewidth = 0.01)
plt.show()