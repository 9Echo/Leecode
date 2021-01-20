# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:23:28 2021

@author: lambda
"""

"""
N 件物品放入容量为 V 的背包，每件物品的容量为c[i]，价值为w[i]，任一 c[i]< V
每件物品只能放置一次，求如何放使得有限容量的背包内的物品价值最大，以及该最大价值value的值
"""
def zero_one_knapsack(c, w, V):
    
    n = len(c)
    
    # dp[i][j] 表示前i件物品，背包容量为j时的最大价值
    dp = [[-1 for i in range(V+1)] for j in range(n)]
    # 初始化当第一件物品放入时dp数值
    for i in range(V+1):
        if c[0] > i:
            dp[0][i] = 0
        else:
            dp[0][i] = w[0]
    
    for i in range(1, n):
        for j in range(V+1):
            dp[i][j] = dp[i-1][j]   
            if c[i] > j:
                continue
            dp[i][j] = max(dp[i-1][j], dp[i][j-c[i]] + w[i])
    
    print(dp)
    
# =============================================================================
#     记录背包中放置了哪些物品
# =============================================================================
    
    path = [-1 for i in range(n)]
    amount = V
    for i in range(n-1, 0, -1):
        if dp[i][amount] == dp[i-1][amount]:
            path[i] = 0
        else:
            path[i] = 1
            amount -= c[i]
    
    if dp[0][amount] == 0:
        path[0] = 0
    else:
        path[0] = 1
    print(path)

    return dp[n-1][V]

if __name__ == "__main__":
    c = [2, 5, 9]
    w = [10, 3, 8]
    V = 7
    result = zero_one_knapsack(c, w, V)
    print(result)
    