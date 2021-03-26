# -*- coding: UTF-8 -*-

from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a).most_common()
    # 1種類の整数しかないとき
    if len(c) == 1:
        print(c[0][1])
    else:
        # 最も多い整数の個数
        most = c[0][1]
        # それ以外の整数の個数総和
        others = 0
        for i in range(1, len(c)):
            others += c[i][1]
        if most < others:
            print(n % 2)
        else:
            print(most - others)