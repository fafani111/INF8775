import util
import re
import conv
import strassen
import strassenSeuil
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-a", type = str, choices = ["conv", "strassen", "strassenSeuil"])
parser.add_argument("-e1", type = str)
parser.add_argument("-e2", type = str)
parser.add_argument("-p", action = "store_true")
parser.add_argument("-t", action = "store_true")
args = parser.parse_args()


m1 = util.readMatrix(args.e1)
m2 = util.readMatrix(args.e2)

init = time.time()

if args.a == "conv":
	m3 = conv.conv(m1, m2)
elif args.a == "strassen":
	m3 = strassen.strassen(m1, m2)
elif args.a == "strassenSeuil":
	m3 = strassenSeuil.strassenSeuil(m1, m2, 2)

end = time.time()
	
if args.p:
	s = str(m3)
	s = re.sub(r"], ", "\n", s)
	s = re.sub(r"[\[\],]+", " ", s)
	s = re.sub(r"^ ", "", s, flags = re.MULTILINE)
	s = re.sub(r"\.*", "", s)
	print(s)
if args.t:
	print((end - init) * 1000)
