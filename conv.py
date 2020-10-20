def conv(a, b):
	c = [[0 for i in range(len(a))] for j in range(len(b[0]))]
	for i in range(0, len(a)):
		for j in range(0, len(b[0])):
			for k in range(0, len(b)):
				c[i][j] += a[i][k] * b[k][j]
	return c
