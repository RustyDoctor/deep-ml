def det(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	else:
		return sum(((-1)**i)*n*det([row[:i]+row[i+1:] for row in matrix[1:]]) for i, n in enumerate(matrix[0]))




def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	return (det(matrix), sum(matrix[i][i] for i in range(len(matrix))))
