from tools.ComplexVectorMatrixClass import Vector, Matrix
from tools.complex_angle_cos import angle_cos

def main():
	u = Vector([complex(2., 5.), complex(1., 8.)])
	v = Vector([complex(4., 1.), complex(2., 9.)])
	print(angle_cos(u, v))

	u = Vector([complex(1., 8.), complex(2., 3.), complex(3., 7.)])
	v = Vector([complex(4., 1.), complex(5., 14.), complex(6., 5.)])
	print(angle_cos(u, v))


if __name__ == "__main__":
	main()