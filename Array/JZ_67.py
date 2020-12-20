# -*- coding:utf-8 -*-
""" JZ—67  剪绳子
题目描述
        给你一根长度为 `n` 的绳子，请把绳子剪成整数长的 `m` 段（`m、n` 都是整数，`n>1` 并且`m>1，m<=n`），
        每段绳子的长度记为 `k[1],...,k[m]`。请问 `k[1]x...xk[m]` 可能的最大乘积是多少？
        例如，当绳子的长度是 `8` 时，我们把它剪成长度分别为 `2、3、3` 的三段，此时得到的最大乘积是 `18`。
"""

# [思路]：对不超过6的正整数number，最大乘积为
# number = 0, max = 0
# number = 1, max = 1
# number = 2, max = 1*1 = 1
# number = 3, max = 1*2 = 2
# number = 4, max = 2*2 = 4
# number = 5, max = 2*3 = 6
# number = 6, max = 3*3 = 9
#
# 对于超过6的正整数number，最大乘积为，尽量将数等分成3份，直接设辅助函数求导。。。
# number = 7, max = 4*3 = 2*2*3 = 12
# number = 8, max = 6*3 = 2*3*3 = 18
# number = 9, max = 9*3 = 3*3*3 = 27
# ...
# number = i, max = max[i-3]*3

class Solution:
    def cutRope(self, number):
        ans = [0, 0, 1, 2, 4, 6, 9]
        if number <= 6:
            return ans[number]
        else:
            for i in range(7, number + 1):
                ans.append(ans[i-3] * 3)
            return ans[-1]