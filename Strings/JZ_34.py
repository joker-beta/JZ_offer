# -*- coding:utf-8 -*-
""" JZ—34 第一层只出现一次的字符
题目描述：
        在一个字符串(`0<=` 字符串长度 `<=10000`，全部由字母组成)中找到第一个只出现一次的字符,
        并返回它的位置, 如果没有则返回 `-1`（需要区分大小写）.（从 `0` 开始计数）
"""
class Solution:
    def FirstNoteRepeatingChar(self, s):
        # 统计每个字符出现的次数
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        # 记录出现次数为1的字符位置
        index = 0
        for j in s:
            if ans[j] == 1:
                return index
            index += 1  # 更新字符串的下标
        return -1