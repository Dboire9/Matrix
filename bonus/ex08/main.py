from tools.ComplexVectorMatrixClass import Matrix

def main():
	u = Matrix([
		[complex(2., 1.), complex(-5., -2.), complex(0., 0.)],
		[complex(4., 0.), complex(3., 3.), complex(7., 0.)],
		[complex(-2., -1.), complex(3., 0.), complex(4., 2.)],
	])
	
	print(u.trace())

	u = Matrix([
		[complex(-2., 4.), complex(-8., 0.), complex(4., -1.)],
		[complex(1., 0.), complex(-23., 5.), complex(4., 0.)],
		[complex(0., 0.), complex(6., -2.), complex(4., 3.)],
	])
	
	print(u.trace())

if __name__ == "__main__":
	main()