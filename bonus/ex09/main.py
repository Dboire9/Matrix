from tools.ComplexVectorMatrixClass import Matrix

def main():

	u = Matrix([
		[complex(1., 2.), complex(3., 4.), complex(5., 6.)],
		[complex(7., 8.), complex(9., 10.), complex(11., 12.)],
		[complex(13., 14.), complex(15., 16.), complex(17., 18.)],
	])

	print(u.transpose())

if __name__ == "__main__":
	main()