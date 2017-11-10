import matplotlib.pyplot as plt
import numpy as np

def scatter_plot(x, title="", xlabel="", ylabel="", colormap="rainbow"):
	
	markers = 1000.0*x[:,2]/max(x[:,2]) 

	plt.set_cmap(colormap)

	plt.scatter(x[:,0],x[:,1],s=markers, c=x[:,2])
	plt.plot()

	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	plt.colorbar()
