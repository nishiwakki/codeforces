# -*- coding: UTF-8 -*-

t = int(input())
for _ in range(t):
    # テストケース入力
    x, y = map(int, input().split())
    # Aliceが先行の分, 勝ち数が1減る
    # 出力
    print(x-1, y)