# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:02:36 2020

@author: pc
"""

def test(num, max_num, min_num):
    if not num:
        return None
    ans = []
    def dfs(l1, front, left):
        n = sum(l1)
        if min_num <= n <= max_num:
            ans.append(l1)
        elif n > max_num or front > left:
            return
        for i in range(0, left-front+1):
            dfs(l1+[num[front+i]], front+i+1, length-1)
    for i in range(len(num)):
        dfs([num[i]], i+1, length-1)
    return ans


num = [16, 22, 30, 29, 24, 33, 8]
length = len(num)
max_num = 33
min_num = 33 * 0.8
print(test(num, max_num, min_num))