# -*- coding: UTF-8 -*-

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if max(x, y) - min(x, y) <= 1:
        print(x + y)
    else:
        print(x + y + (max(x, y) - min(x, y) - 1))