from tools.VectorMatrixClass import *

def main():
	u = Matrix([
		[1., 0.],
		[0., 1.]
	])
	v = Vector([4., 2.])

	print(u.mul_vec(v), '\n')
	
	u = Matrix([
		[2., 0.],
		[0., 2.]
	])
	
	print(u.mul_vec(v), '\n')

	u = Matrix([
		[2., -2.],
		[-2., 2.]
	])
	
	print(u.mul_vec(v), '\n')
	
	u = Matrix([
		[1., 0.],
		[0., 1.]
	])

	v = Matrix([
		[1., 0.],
		[0., 1.]
	])
	
	print(u.copy().mul_mat(v), '\n')
	
	v = Matrix([
		[2., 1.],
		[4., 2.]
	])
	
	print(u.copy().mul_mat(v), '\n')

	u = Matrix([
		[3., -5.],
		[6., 8.]
	])
	
	print(u.copy().mul_mat(v), '\n')



if __name__ == "__main__":
	main()