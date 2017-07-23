# l = ["abc", "ab", "a"]
# print map(len, l)

# def add(n):
#     return n + 1

# l = [1, 2, 3]
# print map(add, l)

# fun = lambda x : x + 1
# print map(fun, l)

# # funkcja anonimowa
# # lambda [argument] : [cialo funkcji]

# adder = lambda x, y : x + y
# print adder(1, 2)

# # opcja 1 -- definicja jawna
# def isEven(n):
#     rem = n % 2
#     return rem == 0

# l = [1, 49, 2, 4, 3, 7]
# res = filter(isEven, l)

# # opcja 2 -- definicja anonimowa
# res = filter(lambda n : (n % 2) == 0, l)
# print res

# l = [1, 2, 3, 4, 5]
# print reduce(lambda n1, n2 : n1 * n2, l)
# print reduce(lambda n1, n2 : n1 + n2, l)

# LIST COMPREHENSION

def modify(n):
    n += 2
    n **= 4
    n /= 2
    return n

def isEven(n):
    rem = n % 2
    return rem == 0

l1 = [1, 2, 3, 4, 5]

# [argument FOR argument IN lista IF WARUNEK]
# [map FOR argument IN lista IF filter]
l2 = [n for n in l1]
print l2, type(l2)

l2 = [n + 1 for n in l1]
print l2

l2 = [modify(n) for n in l1 if isEven(n)]
print l2

tup1 = (1, 2) # (X, Y)
tup2 = (4, 6)
tup3 = (5, 7)

l = [tup1, tup2, tup3]

xList = [t[0] for t in l]
yList = [t[1] for t in l]

print xList, yList
