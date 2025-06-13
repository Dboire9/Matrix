from linear_combination import linear_combination
from tools.VectorMatrixClass import *

def main():
	e1 = Vector([-42., 42])

	print(linear_combination([e1], [-1.]))
	print()
	
	e1 = Vector([-42.])
	e2 = Vector([-42.])
	e3 = Vector([-42.])
	
	print(linear_combination([e1, e2, e3], [-1., 1., 0.]))
	print()
	
	e1 = Vector([-42., 42.])
	e2 = Vector([1., 3.])
	e3 = Vector([10., 20.])
	
	print(linear_combination([e1, e2, e3], [1., -10., -1.]))
	print()
	
	e1 = Vector([-42., 100., -69.5])
	e2 = Vector([1., 3., 5.])

	print(linear_combination([e1, e2], [1., -10.]))
	print()
	
	
if __name__ == "__main__":
	main()