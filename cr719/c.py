# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print(-1)
    else:
        mtx = [0] * n**2
        for i in range(1, n**2+1, 2):
            mtx[i-1] = i//2 + 1
            if n % 2:
                if not i == n**2:
                    mtx[i] = n**2//2 + i//2 + 2
            else:
                mtx[i] = n**2//2 + i//2 + 1
        for i in range(n):
            print(*mtx[i*n:(i+1)*n])