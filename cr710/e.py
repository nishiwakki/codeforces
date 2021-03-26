# -*- coding: UTF-8 -*-

import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    ans_min = [0] * n
    Max, Min = 0, 1
    ok = []
    heapq.heapify(ok)
    for i in range(n):
        if q[i] > Max:
            ans_min[i] = q[i]
            Max = q[i]
            for i in range(Min, Max):
                heapq.heappush(ok, i)
            Min = Max + 1
        else:
            v = heapq.heappop(ok)
            ans_min[i] = v
    ans_max = [0] * n
    Max, Min = 0, 1
    ok = []
    heapq.heapify(ok)
    for i in range(n):
        if q[i] > Max:
            ans_max[i] = q[i]
            Max = q[i]
            for i in range(Min, Max):
                heapq.heappush(ok, -i)
            Min = Max + 1
        else:
            v = heapq.heappop(ok)
            ans_max[i] = -v
    print(*ans_min)
    print(*ans_max)