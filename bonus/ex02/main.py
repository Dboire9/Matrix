from tools.linear_interpolation import lerp
from tools.ComplexVectorMatrixClass import Vector, Matrix

def main():
	print(lerp(21., 42., 0.3))
	print(lerp(0., 1., 0.5))

	v1 = Vector([complex(2., 3.), complex(1., 4.)])
	v2 = Vector([complex(4., 1.), complex(2., 8.)])
	
	m1 = Matrix([[complex(2., 11.), complex(1., 8.)], [complex(3., 4.), complex(4., 2.)]])
	m2 = Matrix([[complex(20., 1.), complex(10., 3.)], [complex(30., 14.), complex(40., 1.)]])

	print(lerp(v1.copy(), v2.copy(), 0.3))
	print()
	print(lerp(m1.copy(), m2.copy(), 0.5))
	
if __name__ == "__main__":
	main()