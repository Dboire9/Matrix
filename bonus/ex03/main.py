from tools.ComplexVectorMatrixClass import Vector, Matrix

def main():
	u = Vector([complex(0., 0.), complex(0., 0.)])
	v = Vector([complex(0., 0.), complex(0., 0.)])
	print(u.dot(v))
	
	u = Vector([complex(1., 1.), complex(1., 1.)])
	v = Vector([complex(1., 1.), complex(1., 1.)])
	print(u.dot(v))
	
	u = Vector([complex(-1., 5.), complex(6., 2.)])
	v = Vector([complex(3., 8.), complex(2., 4)])
	print(u.dot(v))
	
	
if __name__ == "__main__":
	main()