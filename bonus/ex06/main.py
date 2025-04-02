
from tools.cross_products import cross_product
from tools.ComplexVectorMatrixClass import Vector, Matrix

def main():	
	u = Vector([complex(1., 1.), complex(2., 2.), complex(3., 3.)])
	v = Vector([complex(4., 4.), complex(5., 5.), complex(6., 6.)])
	print(cross_product(u, v))
	
	u = Vector([complex(4., 9.), complex(2., 14.), complex(-3., 4.)])
	v = Vector([complex(-2., 4.), complex(-5., -4.), complex(16., -18.)])
	print(cross_product(u, v))

if __name__ == "__main__":
	main()