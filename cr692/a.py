# -*- coding: UTF-8 -*-

'''
gl))hf))))))
      ↑
ここまでの)数が
左の数より多い時Yes
'''

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    s.reverse()
    cnt = 0
    for i in s:
        if not i == ')':
            break
        else:
            cnt += 1
    if cnt > n - cnt:
        print('Yes')
    else:
        print('No')