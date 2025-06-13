from tools.VectorMatrixClass import *

def main():
	u = Vector([0.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()

	u = Vector([1.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()
	
	u = Vector([0., 0.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()
	
	u = Vector([1., 0.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()
	
	u = Vector([2., 1.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()
	
	u = Vector([4., 2.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()
	
	u = Vector([-4., -2.])
	print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print()


if __name__ == "__main__":
	main()