from tools.VectorMatrixClass import Matrix

def main():
	u = Matrix([
		[0., 0., 8.],
		[0., 5., 7.],
		[0., 3., 4.],
	])
	print(u.row_echelon())





if __name__ == "__main__":
	main()