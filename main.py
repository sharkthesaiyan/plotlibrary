import scatter
import matplotlib.pyplot as plt
import numpy as np

def main():
	inputFile = "test.dat"
	x = np.loadtxt(inputFile)
	scatter.scatter_plot(x)
	plt.show()

main()
