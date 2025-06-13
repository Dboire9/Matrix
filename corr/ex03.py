from tools.VectorMatrixClass import *

def main():
	u = Vector([0., 0.])
	v = Vector([0., 0.])
	print(u.dot(v))
	print()
	
	u = Vector([1., 0.])
	v = Vector([0., 0.])
	print(u.dot(v))
	print()
	
	u = Vector([1., 0.])
	v = Vector([1., 0.])
	print(u.dot(v))
	print()
	
	u = Vector([1., 0.])
	v = Vector([0., 1.])
	print(u.dot(v))
	print()
	
	u = Vector([1., 1.])
	v = Vector([1., 1.])
	print(u.dot(v))
	print()
	
	u = Vector([4., 2.])
	v = Vector([2., 1.])
	print(u.dot(v))
	print()
	
if __name__ == "__main__":
	main()