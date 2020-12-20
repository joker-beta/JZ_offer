# -*- coding:utf-8 -*-
""" JZ—52 正则表达式匹配
题目描述
        请实现一个函数用来匹配包括 `'.'` 和 `'*'` 的正则表达式。模式中的字符 `'.'` 表示任意一个字符，
        而 `'*'` 表示它前面的字符可以出现任意次（包含 `0` 次）。在本题中，匹配是指字符串的所有字符匹配整个模式。

        例如，字符串 `"aaa"` 与模式 `"a.a"` 和 `"ab*ac*a"` 匹配，但是与 `"aa.a"` 和 `"ab*a"` 均不匹配。
"""


# [思路一]：递归迭代
class Solution_1:
    """
    s, pattern: string
    """
    def match(self, s, pattern):
        # write code here
        if s == pattern:
            return True
        # 1，若p[1]='*'，那么对s[0]和p[0]比较
        if (len(pattern) > 1) and (pattern[1] == '*'):
            # 1,若s[0]和p[0]能够匹配，考虑到p[1]='*'，那么递归对s[1:]和p[2:]匹配
            if s and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            # 2，若s[0]不能和p[0]匹配，同样考虑到p[1]='*'，那么递归对s和p[2:]匹配
            else:
                return self.match(s, pattern[2:])

        # 2，若字符s和p都非空，并且s[0]和p[0]能够匹配，那么递归对s[1:]和p[1:]进行匹配
        elif s and pattern and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])

        return False





# [思路二]：
#   假设主串为s，长度为sn，模式串为p，长度为pn，对于模式串p当前的第i位来说，有'正常字符'、'*'、'.'三种情况。
#   我们针对这三种情况进行讨论：
#
#       1,如果p[i]为正常字符， 那么我们看s[i]是否等于p[i], 如果相等，说明第i位匹配成功,接下来看s[i+1...sn-1] 和 p[i+1...pn-1]
#       2,如果p[i]为'.', 它能匹配任意字符，直接看s[i+1...sn-1] 和 p[i+1...pn-1]
#       3,如果p[i]为'*'， 表明p[i-1]可以重复0次或者多次，需要把p[i-1] 和 p[i]看成一个整体.
#           3.1 如果p[i-1]重复0次，则直接看s[i...sn-1] 和 p[i+2...pn-1]
#           3.2 如果p[i-1]重复一次或者多次,则直接看s[i+1...sn-1] 和p[i...pn-1]，但是有个前提：s[i]==p[i] 或者 p[i] == '.'
class Solution_2:
    """
    s, pattern: string
    """
    def match(self, s, p):
        # write code here
        sn = len(s)
        pn = len(p)
        # f[i][j]表示s的前i个和p的前j个能否匹配
        f = [[0 for j in range(pn+1)] for i in range(sn+1)]
        for i in range(sn+1):
            for j in range(pn+1):
                # 初始条件：
                # 1，s为空且p为空，为真: f[0][0] = 1
                # 2，s不为空且p为空,为假: f[1..sn][0] = 0
                if j == 0:
                    f[i][j] = (i == 0)
                else:
                    # 如果没有 '*'
                    if p[j-1] != '*':
                        # 对于方法一种的1,2两种情况可知：f[i][j] = f[i-1][j-1]
                        if (i >= 1) and (s[i-1] == p[j-1] or p[j-1] == '.'):
                            f[i][j] = f[i-1][j-1]
                    # 如果有 '*'，第三种情况
                    else:
                        # 重复 0 次，如果重复0次，f[i][j] = f[i][j-2]
                        if j >= 2:
                            f[i][j] = f[i][j] | f[i][j-2]  # 或运算
                        # 重复 1 次或者多次，如果重复1次或者多次，f[i][j] = f[i-1][j]
                        # 这里要用 | 连接， 不然重复 0 次的会直接覆盖
                        if (i >= 1) and (j >= 2) and (s[i-1] == p[j-2] or p[j-2] == '.'):
                            f[i][j] = f[i][j] | f[i-1][j]
        return f[-1][-1]