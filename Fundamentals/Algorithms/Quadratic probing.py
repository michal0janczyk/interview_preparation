"""
    Let h(k) be a hash function that maps an element k to an integer in [0,m-1],
    where m is the size of the table. Let the ith probe position for a value k be given by the function
    h(k,i)=(h(k)+c_{1}i+c_{2}i^{2})mod {m} h(k,i)=(h(k)+c_{1}i+c_{2}i^{2})mod {m}
    where c2 ≠ 0. If c2 = 0, then h(k,i) degrades to a linear probe. For a given hash table, the values of c1 and c2 remain constant.
    Examples:
    If h(k,i)=(h(k)+i+i^{2})mod{m} h(k,i)=(h(k)+i+i^{2}mod{m}, then the probe sequence will be h(k),h(k)+2,h(k)+6,... h(k),h(k)+2,h(k)+6,...
    For m = 2n, a good choice for the constants are c1 = c2 = 1/2, as the values of h(k,i) for i in [0,m-1] are all distinct.
    This leads to a probe sequence of h(k),h(k)+1,h(k)+3,h(k)+6,... h(k),h(k)+1,h(k)+3,h(k)+6,... where the values increase by 1, 2, 3, ...
    For prime m > 2, most choices of c1 and c2 will make h(k,i) distinct for i in [0, (m-1)/2].
    Such choices include c1 = c2 = 1/2, c1 = c2 = 1, and c1 = 0, c2 = 1. Because there are only about m/2 distinct probes for a given element,
    it is difficult to guarantee that insertions will succeed when the load factor is > 1/2.
    Fowler–Noll–Vo hash function
    The current versions are FNV-1 and FNV-1a, which supply a means of creating non-zero FNV offset basis. FNV currently comes in 32-, 64-, 128-, 256-, 512-, and 1024-bit flavors.
    For pure FNV implementations, this is determined solely by the availability of FNV primes for the desired bit length.
    However, the FNV webpage discusses methods of adapting one of the above versions to a smaller length that may or may not be a power of two.
"""

import random
import string

def myHash(s):
    return sum([ord(x) for x in s])

def FVN(s):
    FNV_prime = 0x100000001b3
    offset = 0xcbf29ce484222325

    for i in xrange(len(s)):
        offset = offset * FNV_prime
        offset = offset ^ ord(s[i])

    return offset

class HashTab:
    startSize = 300
    expandFactor = 2.0
    maxLF = 3.0

    A, B = 1, 1

    def __init__(self):
        self._size = self.startSize
        self._tab = [None for _ in xrange(self._size)]
        self._lf = 0.0

        self.searchLen = 0

    def add(self, val):
        assert type(val) == str

        hashVal = FVN(val) % self._size
        a, b = self.A, self.B

        # Szukamy wolnego miejsca i wstawiamy val.
        while True:
            if self._tab[hashVal] is None:
                self._tab[hashVal] = val
                break

            hashVal += a ** b
            hashVal %= self._size

            a += 1
            b += 1

    def search(self, val):
        assert type(val) == str

        hashVal = FVN(val) % self._size
        a, b = self.A, self.B

        # Szukamy naszego elementu lub wolnego miejsca.
        while True:
            if self._tab[hashVal] == val:
                return True
            elif self._tab[hashVal] is None:
                return False

            hashVal += a ** b
            hashVal %= self._size

            a += 1
            b += 1

            self.searchLen += 1

def genString(alphabet, size):
    res = ""

    for i in xrange(size):
        index = random.randint(0, len(alphabet) - 1)
        res += alphabet[index]
    return res

def test(ht):
    maxNum = 100

    for _ in xrange(maxNum):
        s = genString(string.lowercase, 2)
        ht.add(s)

    for _ in xrange(maxNum):
        s = genString(string.lowercase, 2)
        # print("Searching: " + s)

        ht.search(s)

    avg = round(float(ht.searchLen) / maxNum, 2)
    print("Size = {0}; Avg = {1}".format(ht.startSize, avg))

def main():
    for size in xrange(200, 1001, 100):
        ht = HashTab()
        ht.startSize = size

        test(ht)

if __name__ == "__main__":
    main()

# "Reached the unreachable"
