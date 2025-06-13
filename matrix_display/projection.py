from tools.VectorMatrixClass import Vector, Matrix

def main():
	u = Matrix([
	[0. for _ in range(4)] for _ in range(4)
	])
	u = u.projection(120, 1, 1, 1000)
	print(u)
	with open('./proj', 'w') as file:
		for row in u:
			formatted_row = ', '.join(f'{value:.3f}' for value in row)  # Format each value to 3 decimal places
			file.write(formatted_row + '\n')  # Write the row to the file with a newline

if __name__ == "__main__":
	main()