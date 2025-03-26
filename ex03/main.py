from tools.VectorMatrixClass import *

def main():
	u = Vector([0., 0.])
	v = Vector([0., 0.])
	print(u.dot(v))
	
	u = Vector([1., 1.])
	v = Vector([1., 1.])
	print(u.dot(v))
	
	u = Vector([-1., 6.])
	v = Vector([3., 2.])
	print(u.dot(v))
	
	
if __name__ == "__main__":
	main()