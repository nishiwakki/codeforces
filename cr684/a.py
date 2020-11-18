# -*- coding: UTF-8 -*-

t = int(input())
ans = []
for _ in range(t):
    n, c0, c1, h = map(int, input().split())
    s = input()
    # 0の数をカウント
    count0 = s.count('0')
    # 1の数をカウント
    count1 = n - count0
    # 全て0にしたときのコスト
    all0 = n * c0 + count1 * h
    # 全て1にしたときのコスト
    all1 = n * c1 + count0 * h
    # 変更なしのときのコスト
    now = count0 * c0 + count1 * c1
    # 上記3コストいずれかの最小値が答え
    ans.append(min(all0, all1, now))
# 出力
for i in ans:
    print(i)