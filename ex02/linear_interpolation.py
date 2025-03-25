from tools.VectorMatrixClass import Matrix, Vector

def lerp(u, v, t: float):
	if(t == 0):
		return u
	elif(t == 1):
		return v
	if not isinstance(u, Vector) and not isinstance(v, Vector):
		return u + t * (v - u)
	else:
		v.sub(u)
		v.scl(t)
		u.add(v)
		return u