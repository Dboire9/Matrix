from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
	[ 1., -1.],
	[-1., 1.]
	])
	print("Determinant: ", u.determinant())

	u = Matrix([
	[2., 0., 0.],
	[0., 2., 0.],
	[0., 0., 2.]
	])
	print("Determinant: ", u.determinant())
	
	u = Matrix([
	[8., 5., -2.],
	[4., 7., 20.],
	[7., 6., 1.],
	])
	print("Determinant: ", u.determinant())

	u = Matrix([
	[ 8., 5., -2., 4.],
	[ 4., 2.5, 20., 4.],
	[ 8., 5., 1., 4.],
	[28., -4., 17., 1.],
	])
	print("Determinant: ", u.determinant())

if __name__ == "__main__":
	main()