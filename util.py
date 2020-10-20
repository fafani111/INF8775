import io
import conv
import strassen

def readMatrix(fileName):
	with io.open(fileName) as file:
		lines = file.readlines()
		matrix = []
		for i in range(1, len(lines)):
			line = []
			for j in lines[i].split():
				line.append(float(j))
			matrix.append(line)
	return matrix

