from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
		[0., 0.],
		[0., 0.],
	])
	
	print(u.trace())
	print()

	u = Matrix([
		[1., 0.],
		[0., 1.],
	])
	
	print(u.trace())
	print()
	
	u = Matrix([
		[1., 2.],
		[3., 4.],
	])
	
	print(u.trace())
	print()

	u = Matrix([
		[8., -7.],
		[4., 2.],
	])
	
	print(u.trace())
	print()
	
	u = Matrix([
		[1., 0., 0.],
		[0., 1., 0.],
		[0., 0., 1.]
	])
	
	print(u.trace())
	print()



if __name__ == "__main__":
	main()