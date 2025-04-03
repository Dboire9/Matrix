from tools.ComplexVectorMatrixClass import Matrix

def main():
	u = Matrix([
		[complex(8., 2.), complex(5., -4.), complex(-2., 3.)],
		[complex(4., -9.), complex(2.5, 4.), complex(20., 6.)],
		[complex(8., 1.), complex(5., 6.), complex(1., 0.)],
	])
	
	print(u.inverse())
	print()




if __name__== "__main__":
	main()