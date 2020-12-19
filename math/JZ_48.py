# -*- coding:utf8 -*-
"""
题目描述
        写一个函数，求两个整数之和，要求在函数体内不得使用 `+、-、*、/` 四则运算符号。
"""

class Solution:
    def Add(self, num1, num2):
        if (num1 is None) or (num2 is None):
            return None

        while num2 != 0:
            s = (num1 ^ num2)  # 相加，但不考虑进位
            num2 = (num1 & num2) << 1  # 更新进位
            num1 = s & 0xfffffff
        return num1 if (num1 >> 31 == 0) else (num1 - pow(2, 32))

num1 = 1
num2 = 2
print(Solution().Add(num1, num2))