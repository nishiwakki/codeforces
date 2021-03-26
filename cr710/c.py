# -*- coding: UTF-8 -*-

# 最長共通文字列
def lcs(s1, s2):
    len1, len2 = len(s1), len(s2)
    m = [[0] * len2 for _ in range(len1)]
    ret = 0
    for i, ch in enumerate(s1):
        if ch == s2[0]:
            m[i][0] = 1
            ret = 1
    for i, ch in enumerate(s2):
        if ch == s1[0]:
            m[0][i] = 1
            ret = 1
    for i in range(1, len1):
        for j in range(1, len2):
            if s1[i] == s2[j]:
                m[i][j] = m[i-1][j-1] + 1
                ret = max(m[i][j], ret)
            else:
                m[i][j] = 0
    return ret

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    print(len(a) + len(b) - lcs(a, b) * 2)