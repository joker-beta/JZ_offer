# -*- coding:utf8 -*-
""" JZ—44 翻转单词顺序列
题目描述：
        牛客最近来了一个新员工 `Fish`，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
        同事`Cat` 对 `Fish` 写的内容颇感兴趣，有一天他向 `Fish` 借来翻看，但却读不懂它的意思。

        例如，`“student. a am I”`。后来才意识到，这家伙原来把句子单词的顺序翻转了，
        正确的句子应该是 `“ I am a student.”`。
"""

class Solution:
    def ReaverseSentence(self, s):
        if len(s) == 0:
            return ""
        a = list(s.split(' '))
        # 以列表中轴线为基准，对称的元素进行互换
        for i in range(len(a)//2):
            a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]
        return ' '.join(a)

s = 'student. a am I'
print(Solution().ReaverseSentence(s))