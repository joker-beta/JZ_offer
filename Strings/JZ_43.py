# -*- coding:utf-8 -*-
""" JZ—43 左旋字符串
题目描述
        对于一个给定的字符序列 `S`，请你把其循环左移 `K` 位后的序列输出。
        例如，字符序列`S=”abcXYZdef”`,要求输出循环左移 `3` 位后的结果，即 `“XYZdefabc”`。
"""

class Solution:
    def LeftRotateString(self, s, n):
        if len(s) <= 0:
            return ""
        n %= len(s)  # n可能比字符串 S 长度长，移动出现循环
        return s[n:] + s[:n]

s = 'abcXYZdef'
n = 4
print(Solution().LeftRotateString(s, n))