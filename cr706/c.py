# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 入力
    N = int(input())
    mine, diam = [], []
    for n in range(2*N):
        x, y = map(int, input().split())
        # miner's position
        if not x:
            mine.append(abs(y))
        # diamond mine's position
        else:
            diam.append(abs(x))
    # 絶対値が小さい座標順で
    # 計算していくと最短になる
    mine.sort()
    diam.sort()
    ans = 0
    for i in range(N):
        ans += (mine[i]**2 + diam[i]**2) ** 0.5
    # 出力
    print(ans)