class Vector:
	def __init__(self, values):
		self.values = list(values)

	def __str__(self):
		return '\n'.join([str([comp]) for comp in self.values])
	
	def __getitem__(self, index):
		return self.values[index]

	def __setitem__(self, index, value):
		self.values[index] = value

	def add(self, v):
		"""Add another vector to this vector"""
		if len(self.values) != len(v.values):
			raise ValueError("Vectors must have the same length")
		for i in range(len(self.values)):
			self[i] += v[i]

	def copy(self):
		"""Return a copy of this vector"""
		return Vector(self.values.copy())

	def dot(self, v):
		"""Return the dot product of two vectors"""
		if len(self.values) != len(v.values):
			raise ValueError("Vectors must have the same length")
		result = 0
		for i in range(len(self.values)):
			self[i] *= v[i]
			result += self[i]
		return result

	def norm_1(self) -> float:
		result = 0
		for i in range(len(self.values)):
			if(self.values[i] < 0):
				self.values[i] *= -1
			result += self.values[i]
		return result

	def norm(self) -> float:
		result = 0
		for i in range(len(self.values)):
			result += self.values[i]**2
		return result**0.5
	
	def norm_inf(self):
		for i in range(len(self.values)):
			if(self.values[i] < 0):
				self.values[i] *= -1
			self.values[i] = self.values[i]
		return max(self.values)

	def scl(self, K):
		"""Scale this vector by a scalar value"""
		for i in range(len(self.values)):
			self[i] *= K

	def sub(self, v):
		"""Substract another vector to this vector"""
		if len(self.values) != len(v.values):
			raise ValueError("Vectors must have the same length")
		for i in range(len(self.values)):
			self[i] -= v[i]




class Matrix:
	def __init__(self, rows):
		self.rows = [list(row) for row in rows]
		self.num_rows = len(rows)
		self.num_cols = len(rows[0]) if rows else 0
		if not all(len(row) == self.num_cols for row in rows):
			raise ValueError("All rows must have the same length")

	def __str__(self):
		return '\n'.join([f"[{', '.join(map(str, row))}]" for row in self.rows])

	def __getitem__(self, index):
		"""Allow accessing rows using m[i]"""
		return self.rows[index]
	
	def __setitem__(self, index, value):
		"""Allow setting rows using m[io turn in] = value"""
		if len(value) != self.num_cols:
			raise ValueError("Assigned row must match matrix column count")
		self.rows[index] = list(value)
	
	def add(self, v):
		"""Add another matrix to this matrix"""
		if self.num_rows != v.num_rows:
			raise ValueError("Matrices must have same dimensions")
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				self.rows[i][j] += v.rows[i][j]

	def copy(self):
		"""Return a copy of this vector"""
		return Matrix([row.copy() for row in self.rows])

	def mul_vec(self, vec: Vector) -> Vector:
		"""Multiply the matrix by a vector"""
		if self.num_cols != len(vec.values):
			raise ValueError("Length of the vector and the columns in the matrix must be equal")
		result = Vector([0.] * len(vec.values))
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				result[i] += self.rows[i][j] * vec.values[j]
		return result

	def mul_mat(self, mat):
		"""Multiply the two matrices"""
		if self.num_cols != mat.num_rows:
			raise ValueError("Length of the column matrix and the rows in the other must be equal")
		result = Matrix([[0.] * mat.num_cols for _ in range(self.num_rows)])
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				for k in range(mat.num_rows):
					result.rows[i][j] += self.rows[i][k] * mat.rows[k][j]
		return result

	def row_echelon(self):
		result = self.copy()
		# Find the pivot and rearrange the rows
		for i in range(self.num_cols):
			for j in range(self.num_rows):
				if self.rows[j][i] != 0: break
			if self.rows[j][i]: break
		if j != 0:
			for i in range(self.num_cols):
				result.rows[0][i] = self.rows[j][i]
				result.rows[j][i] = self.rows[0][i]
		# Row echelons
		for k in range(self.num_rows):
			j = 0
			result = result.norm_row_echelon(k)
			for j in range(result.num_rows):
				if j != k:
					pivot = result.search_pivot(k)
					result = result.sub_row_echelon(j, k, pivot)
		return result

	def search_pivot(result, k):
		for i in range(result.num_cols):
			if result.rows[k][i] == 1:
				return i
		return 0

	def sub_row_echelon(result, j, k, pivot):
		for i in range(result.num_cols):
			if result.rows[j][pivot] != 0:
				sub = result.rows[j][pivot]
				for i in range(result.num_cols):
					result.rows[j][i] -= sub * result.rows[k][i]
			return result
		return result

	def norm_row_echelon(result, k):
		for j in range(k, result.num_rows):
			for i in range(result.num_cols):
				if result.rows[j][i] != 0:
					divider = 1 / result.rows[j][i]
					start_cols = i
					for i in range(start_cols, result.num_cols):
						result.rows[j][i] *= divider
					return result
		return result

	def scl(self, K):
		"""Scale this matrix by a scalar value"""
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				self.rows[i][j] *= K

	def shape(self):
		"""Return the shape of the matrix in arguments"""
		return f"Matrix {self.num_rows}x{self.num_cols}"

	def sub(self, v):
		"""Substract another matrix to this matrix"""
		if self.num_rows != v.num_rows:
			raise ValueError("Matrices must have same dimensions")
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				self.rows[i][j] -= v.rows[i][j]

	def trace(self) -> float:
		"""Compute the trace of the matrix"""
		if self.num_cols != self.num_rows:
			raise ValueError("The matrix must be a square to do a trace")
		result = 0
		for i in range(self.num_cols):
			result += self.rows[i][i]
		return result

	def transpose(self):
		"""Return the transpose of the matrix"""
		result = Matrix([[0.] * self.num_rows for _ in range(self.num_cols)])
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				result.rows[j][i] = self.rows[i][j]
		return result