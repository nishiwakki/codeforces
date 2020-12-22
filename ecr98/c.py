# -*- coding: UTF-8 -*-

t = int(input())
for _ in range(t):
    s = input()
    ruiseki1 = 0
    ruiseki2 = 0
    ans = 0
    for i in s:
        if i == '(':
            ruiseki1 += 1
        elif i == '[':
            ruiseki2 += 1
        elif i == ')':
            if ruiseki1 > 0:
                ans += 1
                ruiseki1 -= 1
        else:
            if ruiseki2 > 0:
                ans += 1
                ruiseki2 -= 1
    print(ans)