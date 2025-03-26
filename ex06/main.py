from tools.VectorMatrixClass import *
from ex06.cross_products import cross_product

def main():
	u = Vector([0., 0., 1.])
	v = Vector([1., 0., 0.])
	print(cross_product(u, v))
	
	u = Vector([1., 2., 3.])
	v = Vector([4., 5., 6.])
	print(cross_product(u, v))
	
	u = Vector([4., 2., -3.])
	v = Vector([-2., -5., 16.])
	print(cross_product(u, v))




if __name__ == "__main__":
	main()