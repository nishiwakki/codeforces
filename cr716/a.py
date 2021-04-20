# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

square = set()
for i in range(1, 10**4+1):
    square.add(i**2)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = False
    for aa in a:
        if not aa in square:
            ans = True
            break
    if ans:
        print('YES')
    else:
        print('NO')