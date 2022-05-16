import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
#map and map iterator calculator
#a is the relevant parameter (slope)
a=0.7
q = 2-a*np.floor(2/a)
def f(x, n):
	i = 0
	while i < n:
		y = 0
		if 0<=x<q:
			y = 1+a/2-np.sqrt(a**2/4+a*(x+a-q)+a+1-(x+a-q)**2-2*(x+a-q))
		if q<x<=a:
			y = 1+a/2-np.sqrt(a**2/4+a*(x-q)+a+1-(x-q)**2-2*(x-q))
		x = y
		i+=1
	return x

x = []
y = []
x_x = []
y_y = []

#num is number of iterations, tot is number of sample points in the interval [0,a]
num = 1
tot = 10000
plt.rcParams.update({'font.size': 18})
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18) 
for p in np.arange(0, int(q/a*10000), 1):
	print(p)
	x.append(a/tot*p)
	y.append(f(x[p], num))
for p in np.arange(int(q/a*10000)+1, tot, 1):
	x_x.append(a/tot*p)
	y_y.append(f(x_x[p-int(q/a*10000)-1], num))

fig, ax = plt.subplots()
ax.plot(x,y, color ='C0')
ax.plot(x_x,y_y, color ='C0')
ax.plot(x,x, color ='black')
ax.plot(x_x,x_x, color ='black')

plt.xlabel("x")

plt.ylabel("y")
ax.xaxis.set_label_coords(1.02, -.05)
ax.yaxis.set_label_coords(-.1, .9)


plt.show()