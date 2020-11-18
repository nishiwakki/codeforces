# -*- coding: UTF-8 -*-

t = int(input())
ans = []
for _ in range(t):
    # 入力
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 中間値の総和
    val = 0
    # 加算回数（最大でk回）
    cnt = 0
    # 大きい順から数えたときの中間値
    idx = n // 2 + 1
    # 大きい順からidx間隔でチェック
    for i in range(n*k-idx, -1, -idx):
        val += a[i]
        cnt += 1
        if cnt == k:
            break
    ans.append(val)
# 出力
for i in ans:
    print(i)