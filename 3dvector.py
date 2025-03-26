from tools.VectorMatrixClass import *
import matplotlib.pyplot as plt

def main():

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	# Origine et composantes du vecteur
	origin = [0, 0, 0]  # point de départ (x, y, z)
	vector1 = [4., 2., -3.]  # composantes (u, v, w)
	vector2 = [-2., -5., 16.]
	vector3 = [17., -58., -16.]

	# Tracer le vecteur
	ax.quiver(*origin, *vector1, color='r')
	ax.quiver(*origin, *vector2, color='b')
	ax.quiver(*origin, *vector3, color='g')
	
	# Définir les limites des axes
	ax.set_xlim([-50, 30])
	ax.set_ylim([-70, 10])
	ax.set_zlim([-50, 30])
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	
	plt.show()

if __name__ == "__main__":
	main()