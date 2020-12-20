# -*- coding:utf-8 -*-
""" JZ—29  最小的k个数
题目描述：
        输入 `n` 个整数，找出其中最小的 `K` 个数。
        例如输入 `4,5,1,6,2,7,3,8` 这 `8` 个数字，则最小的 `4` 个数字是 `1,2,3,4`。
"""

# [思路]：构建最大堆(每一层从上往下递减)，默认是小顶堆，注意输出时需要逆序。

import heapq as hq

class Solution:
    def GetLeastNumbers(self, arr, k):
        """最小的 k 个数"""
        if (k <= 0) or (k > len(arr)):
            return []
        stack = []  # 记录数组中最小的k个数
        for num in arr:
            if len(stack) < k:
                hq.heappush(stack, -num)
            else:
                if stack[0] < -num:
                    hq.heapreplace(stack, -num)
        ans = []
        while stack:
            ans.append(-hq.heappop(stack))
        return ans[::-1]

    def GetGreastNumbers(self, arr, k):
        """最大的 k 个数"""
        if (k <= 0) or (k > len(arr)):
            return []
        stack = []
        for num in arr:
            if len(stack) < k:
                hq.heappush(stack, num)
            else:
                if stack[0] < num:
                    hq.heapreplace(stack, num)
        ans = []
        while stack:
            ans.append(hq.heappop(stack))
        return ans


a = [4, 5, 1, 6, 2, 7, 3, 8]
k = 5
print('最小%.f个：' %k, Solution().GetLeastNumbers(a, k))
print('最大%.f个：' %k, Solution().GetGreastNumbers(a, k))