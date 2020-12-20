# -*- coding:utf-8 -*-
""" JZ—51  构建乘积数组
题目描述
        给定一个数组 `A[0,1,...,n-1]`,请构建一个数组 `B[0,1,...,n-1]`,
        其中 `B` 中的元素`B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]`。

        不能使用除法。
        （注意：规定 `B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2]`;）
        对于 `A` 长度为 `1` 的情况，`B` 无意义，故而无法构建，因此该情况不会存在
"""

# [思路]：将B数组中每一个元素对应的乘积分成两部分c[i]，d[i]，分别计算
#        B[i] = (A[0]*A[1]*...*A[i-1]) * (A[i+1]*...*A[n-1])
#             = c[i] * d[i]
#
# 计算 c[i]:   c[i] = c[i-1] * A[i-1],   c[0] = 1
# 计算 d[j]:   d[j] = d[j+1] * A[j+1],   d[n-1] = 1

class Solution:
    def multiply(self, A):
        c = [1 for _ in range(len(A))]
        d = [1 for _ in range(len(A))]
        b = []
        for i in range(len(A)-1):
            c[i+1] = c[i] * A[i]
        for j in range(len(A)-2, -1, -1):
            d[j] = d[j+1] * A[j+1]
        for k in range(len(A)):
            b.append(c[k] * d[k])
        return b