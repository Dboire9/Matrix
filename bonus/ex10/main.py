from tools.ComplexVectorMatrixClass import Matrix
from sympy import Matrix as SymMatrix


def main():
	u = Matrix([
		[complex(8., 4.), complex(5., 10.), complex(-2., -5.), complex(4., 9.), complex(28., -12.)],
		[complex(4., 3.), complex(2.5, -7.), complex(20., 6.), complex(4., 1.), complex(-4., 4.)],
		[complex(8., 9.), complex(5., -1.), complex(1., 15.), complex(4., -17.), complex(17., 5.)],
	])
	print(u.reduced_row_echelon())
	print()


	u = SymMatrix([[complex(8, 4), complex(5, 10), complex(-2, -5), complex(4, 9), complex(28, -12)],
				[complex(4, 3), complex(2.5, -7), complex(20, 6), complex(4, 1), complex(-4, 4)],
				[complex(8, 9), complex(5, -1), complex(1, 15), complex(4, -17), complex(17, 5)]])
	print("Verification :", u.rref()[0])  # Use SymPy for exact RREF


if __name__ == "__main__":
	main()