# -*- coding:utf8 -*-
""" JZ—20 包含min函数的栈
题目描述
        定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 `min` 函数
        （时间复杂度应为 `O(1)`）。
"""

# 思路：（待补。。。）

class Solution:
    def __init__(self):
        self.stack = []      # 将每次要比较的元素都压入栈，待定比较
        self.min_stack = []  # 栈尾存放最小值，即该栈为单调递减的栈
        self.length = 0  # 存放栈 stack 的长度

    def isEmpty(self):
        """判断是否为空"""
        return self.length == 0

    def getLength(self):
        """得到栈的长度"""
        return self.length

    def min(self):
        """返回最小值"""
        if self.isEmpty():
            print("Stack is empty!")
            return
        if self.min_stack:
            return self.min_stack[-1]

    def push(self, data):
        """压栈"""
        # 1，若当前待比较的元素不是整数，或者浮点数，说明不满足要求
        if (not isinstance(data, int)) and (not isinstance(data, float)):
            print("The element must be numberic!")
            return
        # 2，若满足要求，则先将待比较元素入栈stack，长度+1，
        #    再通过比较栈stack当前元素和栈min_stack最后元素(当前记录最小元素)，将较小者入栈 min_stack
        else:
            self.stack.append(data)   # 压栈
            self.length += 1    # 栈的长度+1
            # 1，若栈为空，或者要压入栈的元素小于已入栈的最小元素，直接将当前元素压入栈
            if (self.min_stack == []) or (data < self.min()):
                self.min_stack.append(data)
            # 2，否则，将当前对比后较小的元素，压入栈
            else:
                self.min_stack.append(self.min())

    def pop(self):
        """出栈"""
        # 1，若栈 stack 是空的，说明要么还没压入元素，或者栈stack中元素都已经对比处理完毕，直接返回
        if self.isEmpty():
            print("Stack is empty!")
            return
        data = self.stack.pop()
        self.min_stack.pop()
        self.length -= 1
        return data

    def clear(self):
        """清空栈"""
        self.stack = []
        self.min_stack = []
        self.length = 0




