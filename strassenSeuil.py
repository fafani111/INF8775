import conv

def add(a, b):
	return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
	
def sub(a, b):
	return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
	
def appendLine(a, b):
	for i in range(len(a)):
		a[i].extend(b[i])
	return a
	
def merge(c11, c12, c21, c22):
	temp = appendLine(c11, c12)
	temp.extend(appendLine(c21, c22))
	return temp

def strassenSeuil(a, b, seuil):
	if len(a) <= seuil:
		return conv.conv(a, b)
	A = [
		[[line[0:len(a)//2] for line in a[0:len(a)//2]], [line[len(a)//2:len(a)] for line in a[0:len(a)//2]]],
		[[line[0:len(a)//2] for line in a[len(a)//2:len(a)]], [line[len(a)//2:len(a)] for line in a[len(a)//2:len(a)]]]
	]
	B = [
		[[line[0:len(b)//2] for line in b[0:len(b)//2]], [line[len(b)//2:len(b)] for line in b[0:len(b)//2]]],
		[[line[0:len(b)//2] for line in b[len(b)//2:len(b)]], [line[len(b)//2:len(b)] for line in b[len(b)//2:len(b)]]]
	]
	
	m1 = strassenSeuil(sub(add(A[1][0], A[1][1]), A[0][0]), add(sub(B[1][1], B[0][1]), B[0][0]), seuil)
	m2 = strassenSeuil(A[0][0], B[0][0], seuil)
	m3 = strassenSeuil(A[0][1], B[1][0], seuil)
	m4 = strassenSeuil(sub(A[0][0], A[1][0]), sub(B[1][1], B[0][1]), seuil)
	m5 = strassenSeuil(add(A[1][0], A[1][1]), sub(B[0][1], B[0][0]), seuil)
	m6 = strassenSeuil(add(sub(A[0][1], A[1][0]), sub(A[0][0], A[1][1])), B[1][1], seuil)
	m7 = strassenSeuil(A[1][1], add(sub(B[0][0], B[0][1]), sub(B[1][1], B[1][0])), seuil)
	
	c11 = add(m2, m3)
	c12 = add(add(add(m1, m2), m5), m6)
	c21 = sub(add(add(m1, m2), m4), m7)
	c22 = add(add(add(m1, m2), m4), m5)
	
	return merge(c11, c12, c21, c22)
