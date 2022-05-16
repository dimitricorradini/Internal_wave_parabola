import numpy as np
import matplotlib.pyplot as plt
#period finder
#a is slope of trajectory
a=0.7
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
#tot is number of samples in [0, a]
tot = 10000

for n in range(0, tot):
	x = []
	y = []
	print("checking period ", n)
	for p in range(0, tot):
		x.append(a/tot*p)
		y.append(f(x[p], n))
		if ((y[p]-x[p])*(y[p-1]-x[p-1])<0 and not (a-0.1<y[p-1]<a)):
			print("ok")
			break
	if ((y[p]-x[p])*(y[p-1]-x[p-1])<0 and not (a-0.1<x[p-1]<a)):
		print("period found! length is ", n)
		#returns length of period
		break

plt.plot(x,y)
plt.plot(x,x, color = 'black')
plt.show()

