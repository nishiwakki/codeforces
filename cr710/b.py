# -*- coding: UTF-8 -*-

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())
    ans = 0
    idx = 0
    # 最初の'*'をサーチ
    for i in range(n):
        if s[i] == '*':
            s[i] = 'x'
            ans += 1
            idx = i + k
            break
    end = n-1
    # 最後の'*'をサーチ
    for i in range(n-1, -1, -1):
        if s[i] == '*':
            s[i] = 'x'
            ans += 1
            end = i
            break
    # '*'が1つしかないとき
    if ans < 2:
        print(ans)
        continue
    while idx < end:
        if s[idx] == '*':
            s[idx] = 'x'
            ans += 1
            idx += k
        elif s[idx] == 'x':
            idx += k
        # if s[idx] == '.'
        else:
            idx -= 1
    print(ans)