from tools.linear_combination import linear_combination
from tools.ComplexVectorMatrixClass import Vector, Matrix

def main():
	e1 = Vector([complex(1., 1.), complex(0.,0.), complex(0.,0.)])
	e2 = Vector([complex(0.,0.), complex(1., 1.), complex(0.,0.)])
	e3 = Vector([complex(0.,0.), complex(0.,0.), complex(1., 1.)])

	v1 = Vector([complex(1., 1.), complex(2., 2.), complex(3., 3.)])
	v2 = Vector([complex(0., 0.), complex(10., 10.), complex(-100., -100.)])

	print(linear_combination([e1, e2, e3], [complex(10., 10.), complex(-2., -2.), complex(0.5, 0.5)]))
	print(linear_combination([v1, v2], [complex(10., 10.), complex(-2., -2.)]))

if __name__ == "__main__":
	main()