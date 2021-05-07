# -*- coding: UTF-8 -*-

# Same Difference Count
def sd_count(ls, n):
    dic = dict()
    for i in range(n):
        dic[ls[i]-i] = dic.get(ls[i]-i, 0) + 1
    ret = 0
    for x in dic:
        ret += dic[x] * (dic[x]-1) // 2
    return ret

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(sd_count(a, n))