import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

#internal wave parabola simulator
x = np.zeros((50000,))
y = np.zeros((50000,))
x_true = []
y_true = []
y[0]= 0


#a is slope of trajectory
a = -1.04
c = np.sign(a)
print(a)
#random starting point
x[0]=np.random.uniform(-1, 0)

b = -a*x[0]
print(x[0])
x_true.append(x[0])
y_true.append(y[0])
for i in range(1, 5):


    if (y[i-1] > 1-(a*a)/4):
        c *=-1
    x[i] = 1/2*(-a+c*np.sqrt(a*a-4*(b-1)))
    y[i] = 1-x[i]*x[i]
    
    if (y[i]<0):
        c*=-1
        y[i] = 0
        x[i] = -b/a

    #if (i>30000):
    x_true.append(x[i])
    y_true.append(y[i])
    a*=-1
    c*=-1
    b = a*(-x[i])+y[i]
y_par = []
for i in np.arange(-1, 1, 1/20000):
    y_par.append(1-i**2)

plt.rcParams.update({'font.size': 18})
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18) 
fig, ax = plt.subplots()
ax.plot(x_true, y_true, linewidth = 0.5)
ax.plot(np.arange(-1, 1, 1/20000), y_par, color = 'black', linewidth = 1)
ax.plot(np.arange(-1, 1, 1/20000), 0*np.arange(-1, 1, 1/20000), color = 'black', linewidth = 1)
plt.xlabel("x")

plt.ylabel("y")
ax.xaxis.set_label_coords(1.02, -.05)
ax.yaxis.set_label_coords(-.1, .9)

plt.show()