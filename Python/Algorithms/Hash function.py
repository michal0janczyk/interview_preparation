"""
    Hash function
    A hash function is any function that can be used to map data of arbitrary size to data of fixed size.
    The values returned by a hash function are called hash values, hash codes, digests, or simply hashes.
    One use is a data structure called a hash table, widely used in computer software for rapid data lookup.
    Hash functions accelerate table or database lookup by detecting duplicated records in a large file. An example is finding similar stretches in DNA sequences.
    They are also useful in cryptography. A cryptographic hash function allows one to easily verify that some input data maps to a given hash value,
    but if the input data is unknown, it is deliberately difficult to reconstruct it (or equivalent alternatives) by knowing the stored hash value.
    This is used for assuring integrity of transmitted data, and is the building block for HMACs, which provide message authentication.
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
    startSize = 100
    expandFactor = 2.0
    maxLF = 3.0

    def __init__(self):
        self._size = self.startSize
        self._tab = [None for _ in xrange(self._size)]
        self._lf = 0.0

    def add(self, val):
        assert type(val) == str
        hashVal = FVN(val) % self._size

        # Za None wstawiamy wartosc; jesli sa kolizje,
        # to trzeba wstawic liste i trzymac w liscie
        # wszystkie wartosci, ktore daly nam ten sam hash
        if self._tab[hashVal] is None:
            self._tab[hashVal] = [val]
        else:
            self._tab[hashVal] += [val]

        self._lf += 1.0
        if self._lf > self.maxLF:
            self._tab[hashVal]

    def search(self, val):
        # Jesli jest 1 wartosc, to ja zwracamy
        # Jesli byly kolizje, to musimy liniowo przeszukac cala liste
        hashVal = FVN(val) % self._size

        if self._tab[hashVal] == None:
            return None # Element nie wystepuje w tablicy
        else:
            return val in self._tab[hashVal]

    def expand(self): # rehash
        newSize = int(self._size * self.expandFactor)
        newTab = [None] * newSize

        for i in xrange(self._size):
            if self._tab[i]: # Sprawdzamy czy nie jest None.
                for elem in self._tab[i]:
                    newHash = FVN(elem) % newSize

                    if newTab[newHash] is None:
                        newTab[newHash] = [elem]
                    else:
                        newTab[newHash] += [elem]

        self._tab = newTab
        self._size = newSize

def genString(alphabet, size):
    res = ""

    for i in xrange(size):
        index = random.randint(0, len(alphabet) - 1)
        res += alphabet[index]
    return res

def main():
    maxNum = 100
    hashRes = HashTab()

    for x in xrange(maxNum):
        s = genString(string.lowercase, 6)
        hashRes.add(s)

    print hashRes.search("abc")
    print hashRes.search(s)

if __name__ == "__main__":
    main()

# "Reached the unreachable"
