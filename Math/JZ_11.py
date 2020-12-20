# -*- coding:utf-8 -*-
""" JZ-11 二进制中 1 的个数
题目描述：
    输入一个整数，输出该数 `32` 位二进制表示中 `1` 的个数。其中负数用补码表示。
"""

# 思路：(最优解)利用位运算 &: 两个数位都是1时，取1
class Solution:
    def NumberOf1(self, n):
        ans = 0
        while (n&0xfffffff != 0):
            ans += 1
            n = n & (n-1)   # 把最右边的一个数码1转化为0
        return ans

n = 42
print(bin(n))
print(Solution().NumberOf1(n))