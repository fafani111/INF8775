import os
import time
import util
import conv
import strassen
import strassenSeuil

def genMatrix(n):
	for i in range(0, 5):
		os.system("../gen_matrix/Gen " + str(n) + " " + str(i) + ".txt > dump.txt")

def evalMethod(func, matrices):
	times = []
	for i in range(0, 5):
		for j in range(i + 1, 5):
			init = time.time()
			m3 = func(matrices[i], matrices[j])
			end = time.time()
			times.append((end - init) * 1000)
	return times
	
def printStats(n, times, method):
	for i in times:
		print(method, n, i, sep="\t")

def eval():
	for n in range(1, 10):
		genMatrix(n)
		m = [None] * 5
		for j in range(0, 5):
			m[j] = util.readMatrix("./" + str(j) + ".txt")
		
		printStats(n, evalMethod(	conv.conv, m), "conv")
		printStats(n, evalMethod(strassen.strassen, m), "strassen")
		#evalMethod(strassenSeuil.strassenSeuil)

m = [None] * 5
for j in range(0, 5):
	m[j] = util.readMatrix("./" + str(j) + ".txt")

printStats(9, evalMethod(strassen.strassen, m), "strassen")
