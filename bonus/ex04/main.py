from tools.ComplexVectorMatrixClass import Vector, Matrix

def main():
	u = Vector([complex(0., 0.), complex(0., 0.), complex(0., 0.)])
	# print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print(f"Norm_1: {u.norm_1()}")
	print(f"Norm: {u.norm()}")
	print(f"Norm_inf: {u.norm_inf()}")

	u = Vector([complex(1., 1), complex(2., 2), complex(3., 3)])
	# print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print(f"Norm_1: {u.norm_1()}")
	print(f"Norm: {u.norm()}")
	print(f"Norm_inf: {u.norm_inf()}")
	
	u = Vector([complex(-1., 1), complex(-2., 4)])
	# print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
	print(f"Norm_1: {u.norm_1()}")
	print(f"Norm: {u.norm()}")
	print(f"Norm_inf: {u.norm_inf()}")

if __name__ == "__main__":
	main()