from linear_interpolation import lerp
from tools.VectorMatrixClass import *

def main():
	print(lerp(0., 1., 0.))
	print()
	
	print(lerp(0., 1., 1.))
	print()
	
	print(lerp(0., 42., 0.5))
	print()
	
	print(lerp(-42., 42., 0.5))
	print()

	v1 = Vector([-42., 42.])
	v2 = Vector([42., -42.])

	print(lerp(v1.copy(), v2.copy(), 0.5))

if __name__ == "__main__":
	main()