def add(a, b):
	return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
	
def sub(a, b):
	return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
	
def appendLine(a, b):
	for i in range(len(a)):
		a[i].extend(b[i])
	return a
	
def merge(c11, c12, c21, c22):
	##print(len(c11))
	#print(c11, c12, c21, c22)
	temp = appendLine(c11, c12)
	temp.extend(appendLine(c21, c22))
	#print(temp)
	return temp

def strassen(a, b):
	if len(a) == 1:
		return [[a[0][0] * b[0][0]]]
	A = [
		[[line[0:len(a)//2] for line in a[0:len(a)//2]], [line[len(a)//2:len(a)] for line in a[0:len(a)//2]]],
		[[line[0:len(a)//2] for line in a[len(a)//2:len(a)]], [line[len(a)//2:len(a)] for line in a[len(a)//2:len(a)]]]
	]
	B = [
		[[line[0:len(b)//2] for line in b[0:len(b)//2]], [line[len(b)//2:len(b)] for line in b[0:len(b)//2]]],
		[[line[0:len(b)//2] for line in b[len(b)//2:len(b)]], [line[len(b)//2:len(b)] for line in b[len(b)//2:len(b)]]]
	]
	
	m1 = strassen(sub(add(A[1][0], A[1][1]), A[0][0]), add(sub(B[1][1], B[0][1]), B[0][0]))
	m2 = strassen(A[0][0], B[0][0])
	m3 = strassen(A[0][1], B[1][0])
	m4 = strassen(sub(A[0][0], A[1][0]), sub(B[1][1], B[0][1]))
	m5 = strassen(add(A[1][0], A[1][1]), sub(B[0][1], B[0][0]))
	m6 = strassen(add(sub(A[0][1], A[1][0]), sub(A[0][0], A[1][1])), B[1][1])
	m7 = strassen(A[1][1], add(sub(B[0][0], B[0][1]), sub(B[1][1], B[1][0])))
	
	c11 = add(m2, m3)
	c12 = add(add(add(m1, m2), m5), m6)
	c21 = sub(add(add(m1, m2), m4), m7)
	c22 = add(add(add(m1, m2), m4), m5)
	
	return merge(c11, c12, c21, c22)
