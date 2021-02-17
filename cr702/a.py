# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        sma = min(a[i], a[i+1])
        big = max(a[i], a[i+1])
        while sma * 2 < big:
            sma *= 2
            ans += 1
    print(ans)