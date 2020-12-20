# -*- coding:utf-8 -*-
""" JZ—32  把数组排成最小的数
题目描述：
        输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
        例如输入数组 `{3，32，321}`，则打印出这三个数字能排成的最小数字为 `321323`。
"""

# 思路：将两个数字字符串x,y直接拼接对比，
# 	1，若 x+y > y+x，则需要将x和y的位置互换
# 	2，若 x+y < y+x，则不需要互换
# 	3，若 x+y = y+x，则

from functools import cmp_to_key
class Solution_1:
    def Compare_small(self, num1, num2):
        """对比两个字符串形成的整数大小，构成最小排序"""
        if num1 + num2 > num2 + num1:
            return 1
        else:
            return -1

    def PrintMinNumber(self, numbers):
        if numbers is None:
            return ""
        lens = len(numbers)
        if lens == 0:
            return ""
        # 按照cmp_to_key引用排序函数规则进行排序
        tmp_numbers = sorted(numbers, key=cmp_to_key(self.Compare_small))   # 注意这里是函数名
        return int(''.join(tmp_numbers))

a = ['3', '32', '321']
print(Solution_1().PrintMinNumber(a))



class Solution_2:
    def Compare_biger(self, num1, num2):
        """对比两个字符串形成的整数大小，构成最大排序"""
        if num1 + num2 < num2 + num1:
            return 1
        else:
            return -1

    def PrintMaxNumber(self, numbers):
        if numbers is None:
            return ""
        lens = len(numbers)
        if lens == 0:
            return ""
        # 按照cmp_to_key引用排序函数规则进行排序
        tmp_numbers = sorted(numbers, key=cmp_to_key(self.Compare_biger))   # 注意这里是函数名
        return int(''.join(tmp_numbers))

b = ['3', '32', '321']
print(Solution_2().PrintMaxNumber(b))