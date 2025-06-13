from tools.VectorMatrixClass import *

def main():
	u = Matrix([
		[0., 0.],
		[0., 0.]
	])
	v = Vector([4., 2.])

	print(u.mul_vec(v), '\n')
	
	u = Matrix([
		[1., 0.],
		[0., 1.]
	])
	v = Vector([4., 2.])

	print(u.mul_vec(v), '\n')

	u = Matrix([
		[1., 1.],
		[1., 1.]
	])
	v = Vector([4., 2.])
	print(u.mul_vec(v), '\n')
	
	u = Matrix([
		[2., 0.],
		[0., 2.]
	])

	v = Vector([2., 1.])
	print(u.mul_vec(v), '\n')
	
	u = Matrix([
		[0.5, 0.],
		[0., 0.5]
	])

	v = Vector([4., 2.])
	print(u.mul_vec(v), '\n')


if __name__ == "__main__":
	main()