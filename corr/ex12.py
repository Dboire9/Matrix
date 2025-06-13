from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
	[1., 0.],
	[0., 1.]
	])
	
	print(u.inverse())
	print()

	u = Matrix([
	[2., 0.],
	[0., 2.]
	])
	
	print(u.inverse())
	print()

	u = Matrix([
	[0.5, 0.],
	[0., 0.5]
	])
	
	print(u.inverse())
	print()
	
	u = Matrix([
	[0., 1.],
	[1., 0.]
	])
	
	print(u.inverse())
	print()

	u = Matrix([
	[1., 2.],
	[3., 4.]
	])
	
	print(u.inverse())
	print()
	
	u = Matrix([
	[1., 0., 0.],
	[0., 1., 0.],
	[0., 0., 1.]])
	
	print(u.inverse())
	print()





if __name__== "__main__":
	main()