from tools.VectorMatrixClass import *
from cross_products import cross_product

def main():
	u = Vector([0., 0., 0.])
	v = Vector([0., 0., 0.])
	print(cross_product(u, v))
	print()
	
	
	u = Vector([1., 0., 0.])
	v = Vector([0., 0., 0.])
	print(cross_product(u, v))
	print()

	u = Vector([1., 0., 0.])
	v = Vector([0., 1., 0.])
	print(cross_product(u, v))
	print()

	u = Vector([8., 7., -4.])
	v = Vector([3., 2., 1.])
	print(cross_product(u, v))
	print()
	
	u = Vector([1., 1., 1.])
	v = Vector([0., 0., 0.])
	print(cross_product(u, v))
	print()
	
	u = Vector([1., 1., 1.])
	v = Vector([1., 1., 1.])
	print(cross_product(u, v))
	print()
	

if __name__ == "__main__":
	main()