from tools.VectorMatrixClass import Matrix

def main():

	u = Matrix([
	[0., 0.],
	[0., 0.]
	])
	print(u.reduced_row_echelon())
	print()
	
	u = Matrix([
	[1., 0.],
	[0., 1.]
	])
	print(u.reduced_row_echelon())
	print()
	
	u = Matrix([
	[4., 2.],
	[2., 1.]
	])
	print(u.reduced_row_echelon())
	print()
	
	u = Matrix([
	[-7., 2.],
	[4., 8.]
	])
	print(u.reduced_row_echelon())
	print()
	
	u = Matrix([
	[1., 2.],
	[4., 8.]
	])
	print(u.reduced_row_echelon())
	print()



if __name__ == "__main__":
	main()