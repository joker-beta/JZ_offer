# -*- coding:utf-8 -*-
""" JZ—50  数组中重复的数字
题目描述：
        在一个长度为 `n` 的数组里的所有数字都在 `0` 到 `n-1` 的范围内。
        数组中某些数字是重复的，但不知道有几个数字是重复的。
        也不知道每个数字重复几次。请找出数组中第一个重复的数字。
        例如，如果输入长度为7的数组 `{2,3,1,0,2,5,3}`，那么对应的输出是第一个重复的数字 `2`。

返回描述：
        如果数组中有重复的数字，函数返回 `true`，否则返回 `false`。
        如果数组中有重复的数字，把重复的数字放到参数 `duplication[0]` 中。
"""

# [思路]：先创建字典统计数组numbers中各数字出现的次数
#  	     再遍历字典输出第一个统计次数大于1的数字
class Solution:
    def duplicate(self, numbers, duplication):
        ans = {}
        # 统计 numbers 中各数字出现的次数
        for num in numbers:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1

        # 数组中第一个出现的重复数字
        for num in numbers:
            if ans[num] > 1:
                duplication[0] = num
                return True
        return False