#!/usr/bin/python
#Ville Jantunen 2018
#For generating bravais lattices, see main for example
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def genLattice(a,b,c,nx,ny,nz):
	#a,b,c should be numpy arrays of size 3	

	points = []
	for i in range(nx):
		for j in range(ny):
			for z in range(nz):
				points.append(a*i + b*j + c*z)

	return np.asarray(points)

def genCrystal(unit, lattice):
	crystal = []

	for point in lattice:
		for x in unit:
			crystal.append([x[0],x[1]+point[0],x[2]+point[1],x[3]+point[2]])

	return np.asarray(crystal)


def plotCrystal(crystal,xlim=[0,10],ylim=[0,10],zlim=[0,10]):

	fig = plt.figure()
	ax = fig.add_subplot(111,projection="3d")

	ax.set_xlim(xlim)
	ax.set_ylim(ylim)
	ax.set_zlim(zlim)

	for atomType in set(crystal[:,0]):
		atoms = np.asarray([x[1:4] for x in crystal if x[0]==atomType])
		ax.scatter(atoms[:,0].tolist(),atoms[:,1].tolist(),atoms[:,2].tolist(),s=atomType)

	plt.gca().set_aspect('equal', adjustable='box')
	plt.show()

def main():
	#Bravais basis vectors a,b,c
	a = np.asarray([1,0,0])
	b = np.asarray([0,1,0])
	c = np.asarray([0,0,1])
	lattice = genLattice(a,b,c,10,10,10)

	#Atomtypeid is also the plot marker size for that atom type
	#Coordinates relative to each lattive point
	#Unit: [int atomtypenid, x-relative, y-relative, z-relative]

	unit = []
	unit.append([10,0.0,0.25,0.0])
	unit.append([11,0.0,-0.25,0.0])
	unit = np.asarray(unit)
	crystal = genCrystal(unit, lattice)
	plotCrystal(crystal)

if __name__ == "__main__":
	main()
