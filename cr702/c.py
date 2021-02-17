# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

cube = []
for i in range(1, 10**4):
    cube.append(i**3)
cube = set(cube)

t = int(input())
for _ in range(t):
    x = int(input())
    ans = False
    for a in range(1, 10**4):
        b3 = x - a**3
        if b3 in cube:
            ans = True
            break
        if b3 < 1:
            break
    if ans:
        print('YES')
    else:
        print('NO')