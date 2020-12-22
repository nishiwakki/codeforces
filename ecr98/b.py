# -*- coding: UTF-8 -*-

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    min_a_val, min_a_idx = a[0], 0
    for idx, val in enumerate(a):
        total += val
        if val < min_a_val:
            min_a_val = val
            min_a_idx = idx
    max_a_val = max(a)
    ans = 0
    for idx, val in enumerate(a):
        if idx == min_a_idx:
            continue
        ans += max_a_val - val
    ans -= min_a_val
    amari = ((n-1) - (total % (n-1))) % (n-1)
    print(max(0, ans, amari))