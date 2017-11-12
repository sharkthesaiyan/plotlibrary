import plotdefaults
import matplotlib.pyplot as plt
import numpy as np

def main():
	inputFile = "test.dat"
	x = np.loadtxt(inputFile)
	plotdefaults.scatter_plot(x)
	plt.show()

main()
