# -*- coding:utf-8 -*-
""" JZ—42  和为S的两个数
题目描述
        输入一个递增排序的数组和一个数字 $S$，在数组中查找两个数，
        使得他们的和正好是 $S$，如果有多对数字的和等于 $S$，输出两个数的乘积最小的。
"""

# [思路]：双指针想法，由于数组递增排序，设置两个指针在数组两头往内走，
# 	     若出现相加等于S的数字对，进行判断，并存下乘积小的一组

class Solution:
    def FindNumberWithSum(self, array, tsum):
        count = float('INF')
        ans = []
        left, right = 0, len(array)-1
        while left < right:
            s = array[left] + array[right]
            # 若多组相加和等于S，选择乘积最小的一组
            if s == tsum:
                if count >= array[left] * array[right]:
                    count = array[left] * array[right]
                    ans = [array[left], array[right]]
                # 若找到一组，接着让指针往里走，继续更新
                left += 1
                right -= 1
            elif s > tsum:
                right -= 1
            else:
                left += 1
        return ans


