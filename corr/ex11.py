from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
	[0., 0.],
	[0., 0.]
	])
	print("Determinant: ", u.determinant())
	print()

	u = Matrix([
	[1., 0.],
	[0., 1.]
	])
	print("Determinant: ", u.determinant())
	print()
	
	u = Matrix([
	[2., 0.],
	[0., 2.]
	])
	print("Determinant: ", u.determinant())
	print()
	
	u = Matrix([
	[1., 1.],
	[1., 1.]
	])
	print("Determinant: ", u.determinant())
	print()

	u = Matrix([
	[0., 1.],
	[1., 0.]
	])
	print("Determinant: ", u.determinant())
	print()
	
	u = Matrix([
	[1., 2.],
	[3., 4.]
	])
	print("Determinant: ", u.determinant())
	print()
	
	u = Matrix([
	[-7., 5.],
	[4., 6.]
	])
	print("Determinant: ", u.determinant())
	print()
	
	u = Matrix([
	[1., 0., 0.],
	[0., 1., 0.],
	[0., 0., 1.]])
	print("Determinant: ", u.determinant())
	print()

if __name__ == "__main__":
	main()