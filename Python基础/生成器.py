L = [x * x for x in range(10, 0, -2)]
print(L)

print([print(x) for x in range(10, 0, -2)])

G = (x * x for x in range(5))
print(G)

for d in G:
    print(d)


# next(G)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(100))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


for n in odd():
    print(n)

import time


# 无限序列
def infiniteG():
    i = 0
    while True:
        yield i
        i += 1


# for n in infiniteG():
#     print(n, time.time())
#     time.sleep(1)


def triangles():
    n = 1
    L = [1]
    while True:
        yield L
        n += 1

        R = []
        R.append(1)
        for x in range(1, n - 1):
            R.append(L[x - 1] + L[x])
        R.append(1)
        L = R


# for i in triangles():
#      print(i)
#      time.sleep(1)

var = [x * x for x in range(1, 11) if x % 2 == 0]
print(var)

var = [m + n for m in 'ABC' for n in 'XYZ']
print(var)

import os

var = [d for d in os.listdir('..')]
print(var)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
var = [k + '=' + v for k, v in d.items()]
print(var)

L = ['Hello', 'World', 18, 'Apple', None]
var = [s.lower() for s in L if isinstance(s, str)]
print(var)
