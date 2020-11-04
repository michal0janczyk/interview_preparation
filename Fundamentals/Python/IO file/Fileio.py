# f = open("result.dat", "w")
# s = { 2 : 4, "ala" : "kota" }

# f.write(str(s))

# print open("result.dat").read()

import ast

# f = open("result.dat")
# s = f.read()
# s = ast.literal_eval(s)

# print type(s)
# s[2] = 5
# print s

with open("result.dat") as f:
    s = f.read()
    print s

# Stworzmy liste kilku intow [1, 5]
l = [1, 2, 5, 7, 9]
# Wypiszmy do pliku
with open("res.dat", "w") as f:
    f.write(str(l))

# Sczytujemy plik
with open("res.dat") as f:
    s = f.read()

print(s)
l = ast.literal_eval(s)
l = set(l)

# Inty od [1, 10] czy sa w pliku
for n in xrange(1, 10 + 1, 1):
    if n in l:
        print(n)