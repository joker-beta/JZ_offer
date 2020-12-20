# -*- coding:utf8 -*-
""" JZ—54 字符流中第一个不重复的字符
题目描述：
        请实现一个函数用来找出字符流中第一个只出现一次的字符。
        例如，当从字符流中只读出前两个字符 `"go"` 时，第一个只出现一次的字符是 `"g"`。
        当从该字符流中读出前六个字符 `“google"` 时，第一个只出现一次的字符是 `"l"`。
        如果当前字符流没有存在出现一次的字符，返回 `#` 字符。
"""

class Solution:
    def __init__(self):
        self.s = ""
        self.dict1 = {}
    def Insert(self, char):
        """统计字符串中各字符出现的次数"""
        self.s += char
        if char in self.dict1:
            self.dict1[char] += 1
        else:
            self.dict1[char] = 1

    def FirstAppearingOnce(self):
        """返回第一个出现一次的字符"""
        for i in self.s:
            if self.dict1[i] == 1:
                return i
        return '#'