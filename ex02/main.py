from .linear_interpolation import lerp
from tools.VectorMatrixClass import *

def main():
	print(lerp(21., 42., 0.3))
	print(lerp(0., 1., 0.5))

	v1 = Vector([2., 1.])
	v2 = Vector([4., 2.])

	print(lerp(v1.copy(), v2.copy(), 0.3))
	print(v1, '\n', v2)

	
	
if __name__ == "__main__":
	main()