# -*- coding: UTF-8 -*-

t = int(input())
for _ in range(t):
    n = int(input())
    # LCM(1...9) = 2520
    for i in range(n, n + 2521):
        ii = map(int, str(i))
        if all(iii == 0 or i % iii == 0 for iii in ii):
            print(i)
            break
