import collections
l = [1, 2, 2, 4, 3, 1, 2, 5, 3, 4, 6, 1]

c = collections.Counter(l)

print l

for (k,v) in c.items():
    if v % 2:
        print k, v

