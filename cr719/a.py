# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    t = input().rstrip('\n')
    tasks = [0] * 26
    ans = True
    last = None
    for tt in t:
        if tasks[ord(tt)-65]:
            if not tt == last:
                ans = False
                break
        else:
            tasks[ord(tt)-65] += 1
            last = tt
    if ans:
        print('YES')
    else:
        print('NO')