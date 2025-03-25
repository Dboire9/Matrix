from .linear_combination import linear_combination
from tools.VectorMatrixClass import *
import numpy as np
import matplotlib.pyplot as plt

def main():
	e1 = Vector([1., 0., 0.])
	e2 = Vector([0., 1., 0.])
	e3 = Vector([0., 0., 1.])

	v1 = Vector([1., 2., 3.])
	v2 = Vector([0., 10., -100.])

	print(linear_combination([e1, e2, e3], [10., -2., 0.5]))

	print(linear_combination([v1, v2], [10., -2.]))
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	# Origine et composantes du vecteur
	origin = [0, 0, 0]  # point de départ (x, y, z)
	vector1 = [1., 2., 3.]  # composantes (u, v, w)
	vector2 = [0., 10., -100.]
	vector3 = [10., 0., 230.]

	# Tracer le vecteur
	ax.quiver(*origin, *vector1, color='r')
	ax.quiver(*origin, *vector2, color='b')
	ax.quiver(*origin, *vector3, color='g')
	
	# Définir les limites des axes
	ax.set_xlim([0, 150])
	ax.set_ylim([0, 100])
	ax.set_zlim([-105, 235])
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	
	plt.show()

if __name__ == "__main__":
	main()