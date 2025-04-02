from .linear_interpolation import lerp
from tools.VectorMatrixClass import *

def main():
	print(lerp(21., 42., 0.3))
	print(lerp(0., 1., 0.5))

	v1 = Vector([2., 1.])
	v2 = Vector([4., 2.])
	
	m1 = Matrix([[2., 1.], [3., 4.]])
	m2 = Matrix([[20., 10.], [30., 40.]])

	print(lerp(v1.copy(), v2.copy(), 0.3))
	print()
	print(lerp(m1.copy(), m2.copy(), 0.5))

if __name__ == "__main__":
	main()