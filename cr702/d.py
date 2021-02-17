# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    stack = [(0, n, -1)]
    while stack:
        start, end, root = stack.pop()
        if start + 1 == end:
            if not root == -1:
                ans[start] = ans[root] + 1
        elif not start == end:
            target = a[start:end]
            next_root = start + target.index(max(target))
            if not root == -1:
                ans[next_root] = ans[root] + 1
            stack.append((next_root+1, end, next_root))
            stack.append((start, next_root, next_root))
    print(*ans)