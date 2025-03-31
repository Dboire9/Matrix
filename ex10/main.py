from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
	[8., 5., -2., 4., 28.],
	[4., 2.5, 20., 4., -4.],
	[8., 5., 1., 4., 17.],
	])
	print(u.row_echelon())

	u = Matrix([
	[1., 2.],
	[2., 4.],
	])
	print(u.row_echelon())



if __name__ == "__main__":
	main()