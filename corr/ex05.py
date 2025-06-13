from tools.VectorMatrixClass import *
from tools.complex_angle_cos import angle_cos

def main():
	u = Vector([1., 0.])
	v = Vector([0., 1.])
	print(angle_cos(u, v))
	print()

	u = Vector([8., 7.])
	v = Vector([3., 2.])
	print(angle_cos(u, v))
	print()


	u = Vector([1., 1.])
	v = Vector([1., 1.])
	print(angle_cos(u, v))
	print()
	
	u = Vector([4., 2.])
	v = Vector([1., 1.])
	print(angle_cos(u, v))
	print()
	
	u = Vector([-7., 3.])
	v = Vector([6., 4.])
	print(angle_cos(u, v))
	print()
	
	v = Vector([1., 1.])
	u = Vector([4., 2.])
	print(angle_cos(u, v))
	print()
	
	v = Vector([6., 4.])
	u = Vector([-7., 3.])
	print(angle_cos(u, v))
	print()


if __name__ == "__main__":
	main()