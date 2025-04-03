from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
	[1., 0., 0.],
	[0., 1., 0.],
	[0., 0., 1.]
	])
	
	print(u.inverse())
	print()

	u = Matrix([
	[2., 0., 0.],
	[0., 2., 0.],
	[0., 0., 2.]
	])
	
	print(u.inverse())
	print()

	u = Matrix([
	[8., 5., -2.],
	[4., 7., 20.],
	[7., 6., 1.]
	])
	
	print(u.inverse())
	print()




if __name__== "__main__":
	main()