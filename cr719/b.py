# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans, cnt = 0, 1
    while n >= cnt:
        ans += min(cnt*9, n) // cnt
        cnt = cnt*10 + 1
    print(ans)