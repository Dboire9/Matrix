from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
	[8., 5., -2., 4., 28.],
	[4., 2.5, 20., 4., -4.],
	[8., 5., 1., 4., 17.],
	])
	print(u.reduced_row_echelon())
	print()
	u = Matrix([
	[0., 0., 0.],
	[0., 1., 0.],
	[0., 0., 0.],
	])
	print(u.reduced_row_echelon())



if __name__ == "__main__":
	main()