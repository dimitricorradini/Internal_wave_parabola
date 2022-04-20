import numpy as np
import matplotlib.pyplot as plt

a=0.48
q = 2-a*np.floor(2/a)
def f(x, n):
	i = 0
	while i < n:
		y = 0
		if 0<x<q:
			y = 1+a/2-np.sqrt(a**2/4+a*(x+a-q)+a+1-(x+a-q)**2-2*(x+a-q))
		if q<x<a:
			y = 1+a/2-np.sqrt(a**2/4+a*(x-q)+a+1-(x-q)**2-2*(x-q))
		x = y
		i+=1
	return x

x = []
y = []


for p in range(0, 50):
	x.append(a/100000*p)
	y.append(f(x[p], 1000000))
	print(p)

plt.plot(x,y)
plt.plot(x,x)
plt.show()