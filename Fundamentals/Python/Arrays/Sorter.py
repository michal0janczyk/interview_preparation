import random
import sys

N = 1000 # Array size
I = 10000 # iterations
M = 100000 # Max number value

sU = 0.0 # avg #comparisons, unsorted
sS = 0.0 # avg #comparisons, sorted

l = []
for j in xrange(N):
    l += [random.randint(0, M)]

for i in xrange(I):
    perc = round(100.0 * (i + 1) / I, 2)
    sys.stdout.write("\r{0}/{1} ({2}%)".format(i, I, perc))

    toSearch = random.randint(0, M)
    found = False

    for j in xrange(N):
        if l[j] == toSearch:
            sU += (j + 1)
            found = True
            break

    if not found:
        sU += N

l = sorted(l)
print ""

for i in xrange(I):
    perc = round(100.0 * (i + 1) / I, 2)
    sys.stdout.write("\r{0}/{1} ({2}%)".format(i, I, perc))
  
    toSearch = random.randint(0, M)
    found = False

    for j in xrange(N):
        if l[j] >= toSearch:
            sS += (j + 1)
            found = True
            break

    if not found:
        sS += N

sU /= I
sS /= I

print("\nSU = {0}, SS = {1}".format(sU, sS))
