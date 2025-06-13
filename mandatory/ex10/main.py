from tools.VectorMatrixClass import Matrix

def main():

	u = Matrix([
	[8., 5.5, -2.],
	[4., 6, 9.],
	[4., 5., 123.],
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