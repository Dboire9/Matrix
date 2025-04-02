from tools.ComplexVectorMatrixClass import Vector, Matrix

def main():
	u = Vector([complex(2.0, 1.0), complex(3.0, 2.0)])
	v = Vector([complex(5., 3.0), complex(7., 4.0)])
	u.add(v)
	print(f"add: \n{u}")
	print()

	u = Vector([complex(2.0, 1.0), complex(3.0, 2.0)])
	v = Vector([complex(5., 3.0), complex(7., 4.0)])
	u.sub(v)
	print(f"sub: \n{u}")
	print()
	
	u = Vector([complex(2.0, 1.0), complex(3.0, 2.0)])
	u.scl(2.0)
	print(f"scl: \n{u}")
	print()

	u = Matrix([
	[complex(1., 2.), complex(2.,3.)],
	[complex(3.,4.), complex(4.,5)]
	])

	v = Matrix([
	[complex(7., 8.), complex(4., 6)],
	[complex(-2., 1), complex(2., 7)]
	])
	
	print(v.shape())
	u.add(v)
	print(f"add: \n{u}")
	print()

	u = Matrix([
	[complex(1., 2.), complex(2.,3.)],
	[complex(3.,4.), complex(4.,5)]
	])

	v = Matrix([
	[complex(7., 8.), complex(4., 6)],
	[complex(-2., 1), complex(2., 7)]
	])
	
	u.sub(v)
	print(f"sub : \n{u}")
	print()
	
	u = Matrix([
	[complex(1., 2.), complex(2.,3.)],
	[complex(3.,4.), complex(4.,5)]
	])
	u.scl(2.)
	print(f"scl : \n{u}")

if __name__ == "__main__":
	main()