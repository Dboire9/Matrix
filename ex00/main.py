from .VectorMatrixClass import Vector, Matrix

def main():
	u = Vector([2., 3.])
	v = Vector([5., 7.])
	
	u.add(v)
	print(u)
	
	u = Vector([2., 3.])
	v = Vector([5., 7.])
	
	u.sub(v)
	print(u)
	
	u = Vector([2., 3.])
	u.scl(2.)
	
	print(u)


	u = Matrix([
	[1., 2.],
	[3., 4.]
	])

	v = Matrix([
	[7., 4.],
	[-2., 2.]
	])
	
	print(v.shape())

	u.add(v)
	print(u)
	
	u = Matrix([
	[1., 2.],
	[3., 4.]
	])

	v = Matrix([
	[7., 4.],
	[-2., 2.]
	])

	u.sub(v)
	print(u)

	u = Matrix([
	[1., 2.],
	[3., 4.]
	])
	print("scl")
	u.scl(2.)
	print(u)


if __name__ == "__main__":
	main()