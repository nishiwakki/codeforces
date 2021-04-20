# -*- coding: UTF-8 -*-

from math import gcd

n = int(input())
ans = []
cal = 1
for i in range(1, n-1):
    if gcd(i, n) == 1:
        ans.append(i)
        cal = cal * i % n
cal = cal * (n-1) % n
if cal == 1:
    ans.append(n-1)
print(len(ans))
print(*ans)

'''
[    SIMULATION     ]
[~ bruteforce(bit) ~]
from itertools import product
for n in range(2, 20):
    cnt = 0
    pat = None
    pr = list(product(range(2), repeat=n-1))[1:]
    for p in pr:
        cal = 1
        for i in range(n-1):
            if p[i]:
                cal *= i+1
        bit = p.count(1)
        if cal % n == 1:
            if bit > cnt:
                cnt = bit
                pat = p
    res = []
    for i in range(n-1):
        if pat[i]:
            res.append(i+1)
    print(n, res)
'''