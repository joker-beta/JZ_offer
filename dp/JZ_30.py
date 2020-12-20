# -*- coding:utf-8 -*-
""" JZ—30 连续子数组的最大和(连续子序列)

题目描述：
        给一个数组，返回它的最大连续子序列的和

例子：
	输入: [1,-2,3,10,-4,7,2,-5]
	返回值: 18
"""

class Solution:
    def FindGreatstSumOfSubArray(self, array):
        # dp[i] 表示以array[i]结尾的子序列构成的最大和
        dp = [0 for i in range(len(array))]
        dp[0] = array[0]
        # 若前i-1个数累加和大于零，则继续往后添加，否则以当前元素array[i] 作为新的子序列的起始点
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1], 0) + array[i]
        return max(dp)