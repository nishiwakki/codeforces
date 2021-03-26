# -*- coding: UTF-8 -*-

from math import ceil
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    if x % n == 0:
        row = n - 1
    else:
        row = x % n - 1
    col = ceil(x / n)
    print(row * m + col)