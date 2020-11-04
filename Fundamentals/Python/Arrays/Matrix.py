import numpy as np

delimiter = ' '

mat = [[1,2], [3,4]]

with open("mat.dat", "a") as f:
     for r in mat:
         for v in r:
             f.write(str(v) + delimiter)
         f.write('\n')

with open("mat.dat", "r") as f:
     data = f.read().split('\n')

data = [d.strip(delimiter) for d in data if d]
mat = []

for r in data:
     mat += [[int(n) for n in r.split(delimiter)]]

mat = np.fromfile("mat.dat", dtype = int, count=-1, sep=' ')
mat = np.loadtxt("mat.dat", dtype = int, delimiter=' ')

print mat
print mat.shape

print np.linalg.det(mat)
Sum = 5.0

import sys

s = 0.0


for i in xrange(1, len(sys.argv) , 1):
    s += float(sys.argv[i])

print "Sum = {0}" .format(s)
