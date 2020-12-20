# -*- coding:utf-8 -*-
""" JZ—5 两个栈实现队列
题目描述：
        用两个栈来实现一个队列，完成队列的 `Push` 和 `Pop` 操作。 队列中的元素为 `int` 类型。
"""

class Solution:
    def __init__(self):
        self.stockA = []
        self.stockB = []

    def push(self, node):
        """入栈"""
        self.stockA.append(node)

    def pop(self):
        """出栈"""
        if self.stockB == []:
            # 1，若两个栈都为空，直接返回None
            if self.stockA == []:
                return None
            # 2，若此时 stockA 非空，那么对该栈进行出栈操作，即将 stockA中元素反向添加到stockB中
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()
