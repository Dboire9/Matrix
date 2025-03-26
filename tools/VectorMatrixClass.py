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
	