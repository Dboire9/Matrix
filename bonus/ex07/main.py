from tools.ComplexVectorMatrixClass import *

def main():
	u = Matrix([
		[complex(1., 0.), complex(0., 0.)],
		[complex(0., 0.), complex(1., 0.)]
	])
	v = Vector([complex(4., 2.), complex(2., 4.)])
	print(u.mul_vec(v), '\n')
	
	v = Matrix([
	[2., 1.],
	[4., 2.]
	])
	
	u = Matrix([
	[complex(3., 6.), complex(-5., 4.)],
	[complex(6., -7.), complex(8., -2.)]
	])
	
	print(u.copy().mul_mat(v), '\n')



if __name__ == "__main__":
	main()