# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 入力
    n, k = map(int, input().split())
    s = input()
    # k=0: 反転チェックいらない
    if not k:
        print('YES')
        continue
    # ak+1分の文字が足りない
    if n == k*2:
        print('NO')
        continue
    flg = True
    # 最初k文字をチェック
    for i in range(k):
        j = n - i - 1
        if not s[i] == s[j]:
            flg = False
    # 出力
    if flg:
        print('YES')
    else:
        print('NO')