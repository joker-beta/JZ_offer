# -*- coding:utf-8 -*-
""" JZ—10 矩形覆盖
题目描述：
        我们可以用 `2x1` 的小矩形横着或者竖着去覆盖更大的矩形。
        请问用 `n` 个 `2x1` 的小矩形无重叠地覆盖一个 `2xn` 的大矩形，总共有多少种方法？
"""

# [思路]：dp[i] 表示覆盖 2xi 大矩形的方法数
#       1，若第一个小矩形竖着放，此时后面2x(i-1)大矩形有 dp[i-1] 种覆盖方法
#       2，若第一个小矩形横着放，那么必定前两个小矩形都是横着放，所以后面2x(i-2)大矩形有 dp[i-2] 种覆盖方法
#  所以合并起来的转移方程就是：dp[i] = dp[i-1] + dp[i-2]

class Solution_1:
    def rectCover(self, n):
        if n <= 0:
            return 0
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]



# （做点优化）进一步可以将dp数组简化为三个变量
class Solution_2:
    def rectCover(self, n):
        if n <= 0:
            return 0
        fast = slow = 1
        for i in range(2, n+1):
            tmp = fast
            fast += slow
            slow = tmp
        return fast

n = 6
print(Solution_2().rectCover(n))