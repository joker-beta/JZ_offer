# -*- coding：utf8 -*-
""" JZ—49 把字符串转换成整数
题目描述：
        将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
        数值为 `0` 或者字符串不是一个合法的数值则返回 `0`
"""

# [思路]：
#   1，建立 list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#   2，每个字符在 list 里面寻找他的索引，这个索引就是它对应的值

class Solution:
    def StrToInt(self, s):
        """判断字符串是否为数字"""
        if len(s) == 0:
            return 0
        List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   # 或者 list(map(str, range(10))
        flag = 1  # 记录正负号
        ans = 0   # 存放拼接的数字

        # 判断第一位是否为正负号，或者数字，或者其他
        if s[0] == '+':
            flag = 1
        elif s[0] == '-':
            flag = -1
        elif (s[0] > '0') and (s[0] < '9'):
            ans += List.index(s[0]) * pow(10, len(s)-1)   # 最高位
        else:
            return 0   # 若字符首位不是'+/-'，或者数字字符，说明字符串不合法

        # 若字符串合法，进行每个数位的合并
        for i in range(1, len(s)):
            if (s[i] >= '0') and (s[i] <= '9'):
                ans += List.index(s[i]) * pow(10, len(s)-1-i)
            else:
                return 0
        return flag * ans

s = '+12456'
#s ='+12f3f'
print(Solution().StrToInt(s))