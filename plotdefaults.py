import matplotlib.pyplot as plt
import numpy as np

def default_plot(x,y,order=1,n=100, silent=1):
	#Assuming x and y as normal one dimensional data-arrays of floats or integers
	#2:nd order plots are prettier with larger n.
	#first and second order plots as these are the most common ones we wan't to
	#see often	

	x1 = np.linspace(x[0],x[-1],n)
	if(order==1):
		k = np.polyfit(x,y,1)
		y1 = k[0]*x1 + k[1]		

	elif(order==2):
		k = np.polyfit(x,y,2)
		y1 = k[0]*(x1**2) + k[1]*x1 + k[2]

	if(silent==0):
		print k

	plt.plot(x,y,'ro')
	plt.plot(x1,y1)

	return k

def scatter_plot(x, title="", xlabel="", ylabel="", colormap="rainbow"):
	
	markers = 1000.0*x[:,2]/max(x[:,2]) 

	plt.set_cmap(colormap)

	plt.scatter(x[:,0],x[:,1],s=markers, c=x[:,2])
	plt.plot()

	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.colorbar()
