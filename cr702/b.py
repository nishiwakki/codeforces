# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rem = [0] * 3
    for i in a:
        rem[i%3] += 1
    ans = 0
    for __ in range(2):
        for i in range(3):
            if rem[i] > n//3:
                dec = rem[i] - n//3
                rem[i] -= dec
                rem[(i+1)%3] += dec
                ans += dec
    print(ans)