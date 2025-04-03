from tools.VectorMatrixClass import *

def main():
	u = Vector([0., 0., 0.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

	u = Vector([1., 2., 3.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	
	u = Vector([-1., -2.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")


if __name__ == "__main__":
	main()