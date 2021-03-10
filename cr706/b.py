# -*- coding: UTF-8 -*-

# 切り上げ
from math import ceil
import sys
input = sys.stdin.readline

t = int(input())
for t in range(t):
    # 入力
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # k=0のとき操作せず
    if not k:
        print(n)
        continue
    # 昇順ソート
    a.sort()
    # mex(a)
    mex = 0
    for i in a:
        if i == mex:
            mex += 1
        else:
            break
    # 0...MAXまであるとき
    if mex == n:
        print(n+k)
    else:
        S = set(a+[ceil((mex+max(a))/2)])
        print(len(S))