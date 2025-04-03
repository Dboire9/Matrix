from tools.ComplexVectorMatrixClass import Matrix

def main():
	u = Matrix([
		[complex(8., 2.), complex(5., -4.), complex(-2., 3.), complex(4., 11.)],
		[complex(4., -9.), complex(2.5, 4.), complex(20., 6.), complex(4., -8.)],
		[complex(8., 1.), complex(5., 6.), complex(1., 0.), complex(4., 8.)],
		[complex(28., 3.), complex(-4., 7.), complex(17., -12.), complex(1., 7.)],
	])
	
	print(u.rank())




if __name__ == "__main__":
	main()