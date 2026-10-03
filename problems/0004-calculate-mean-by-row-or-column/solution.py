def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		return [sum(i)/len(i) for i in matrix]
	elif mode == 'column':
		return [sum([j[i] for j in matrix])/len(matrix) for i in range(len((matrix[0])))]