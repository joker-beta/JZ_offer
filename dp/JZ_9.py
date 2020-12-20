# -*- coding:utf-8 -*-
""" JZ—9 变态跳台阶
题目描述：
        一只青蛙一次可以跳上 `1` 级台阶，也可以跳上 `2` 级……它也可以跳上 `n` 级。
        求该青蛙跳上一个 `n` 级的台阶总共有多少种跳法。
"""

# [思路]：dp[i] 表示i个台阶的跳法数
#       dp[i] = dp[i-1] + dp[i-2] + ... + dp[1]
#       dp[i-1] = dp[i-2] + dp[i-3] + ... + dp[1]
#  ==> dp[i] = 2 * dp[i-1], dp[1] = 1
#  ==> dp[i] = 2^(i-1)

class Solution:
    def JumpFloorII(self, number):
        dp = [1 for i in range(number)]
        for i in range(1, number):
            dp[i] = 2 * dp[i-1]
        return dp[-1]




""" 扩展（商汤2018年笔试）
题目描述：
        有n级台阶，每次最多跳m级台阶，其中 0 < m <= n，计算总共的跳法数
"""

# [思路]：dp[i] 表示i个台阶的跳法数
#       dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-m]
class Solution_1:
    def JumpFloorIII(self, n, m):
        if (n <= 0) or (n < m):
            return -1
        if (n == 1) or (m == 1):
            return 1
        elif n == 2:
            if m == 1:
                return 1
            elif m == 2:
                return 2
        else:
            dp = [i for i in range(n)]    # 由于从前往后累加，并且dp[0]=0, dp[1]=1, dp[2]=2
            for i in range(n):
                for j in range(i-1, i-1-m, -1):
                    if j >= 0:
                        dp[i] += dp[j]
            return dp[-1]

n = 4
m = 3
print(Solution_1().JumpFloorIII(n, m))
