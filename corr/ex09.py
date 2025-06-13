from tools.VectorMatrixClass import Matrix

def main():

	u = Matrix([
	[0., 0.],
	[0., 0.]
	])

	print(u.transpose())
	print()
	
	u = Matrix([
	[1., 0.],
	[0., 1.]
	])

	print(u.transpose())
	print()
	
	u = Matrix([
	[1., 2.],
	[3., 4.]
	])

	print(u.transpose())
	print()

	u = Matrix([
	[1., 0., 0.],
	[0., 1., 0.],
	[0., 0., 1.]
	])

	print(u.transpose())
	print()
	
	u = Matrix([
	[1., 2.],
	[3., 4.],
	[5., 6.]
	])

	print(u.transpose())
	print()





if __name__ == "__main__":
	main()