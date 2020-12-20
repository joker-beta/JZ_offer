# -*- coding:utf8 -*-
""" JZ—53 表示数值的字符串
题目描述：
        请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

        例如，字符串 `"+100","5e2","-123","3.1416"` 和 `"-1E-16"` 都表示数值。
        但是 `"12e","1a3.14","1.2.3","+-5"` 和 `"12e+4.3"` 都不是。
"""

# [思路一]：分析不满足要求的情况
#       1，12e：说明 e 的后面必须有数字，不能有两个 e
#       2，+-5：说明符号位要么出现一次在首位，要么出现一次在 e 的后一位，其他地方都不能有
#       3，12e4.3：说明 e 的后面不能有小数
#       4，1.2.3：说明不能有两个小数点
#       5，1a3.14：说明不能有其他的非法字符，比如这里的 a
class Solution_1:
    def isNumeric(self, s):
        sign = 0   # 记录+-符号之前是否出现过
        point = 0  # 记录小数点.之前是否出现过
        letterE = 0  # 记录e或者E之前是否出现过

        # 分析不满足条件的情况
        for i in range(len(s)):
            # 1，若当前字符为 +-
            if s[i] in '+-':
                # 1.1 若字符 +- 之前没有出现过，并且前一个位置不是 e或者E，那么不满足要求
                if (sign == 0) and (i > 0) and (s[i-1] not in 'eE'):
                    return False
                # 1.2 若字符之前出现过，但是前一个位置不是 e或者E，那么满足要求
                elif (sign == 1) and (s[i-1] not in 'eE'):
                    return False
                sign = 1  # 将符号标记为出现过

            # 2，若当前字符为 数字
            elif s[i].isdigit():
                pass

            # 3，若当前字符为 小数点
            elif s[i] == '.':
                # 若之前已经出现过字符e或者E，又或者出现过小数点，都不满足条件
                if (point == 1) or (letterE == 1):
                    return False
                point = 1  # 将小数点标记为出现过

            # 4，若当前字符为 e或者E
            elif s[i] in 'eE':
                # 若之前已经出现过字符e或者E，又或者前一个字符不是数字，又或者当前已经遍历到最后一个字符
                if (letterE == 1) or (not s[i-1].isdigit()) or (i == len(s)-1):
                    return False
                letterE = 1  # 将e/E标记为出现过

            # 5，若当前字符不是符号+-，数字，小数点，e/E，说明不满足要求
            else:
                return False
        # 除去以上分析的情况，其余情况都满足要求
        return True

#s = "1a3.14"
s = "1e2"
print(Solution_1().isNumeric(s))



# [思路二]：内置函数 float()
class Solution_2:
    def isNumeric(self, s):
        try:
            ans = float(s)   # 如果能直接转为浮点型，说明输入字符串满足条件
            return True
        except:
            return False

ss = '123e31'
print(Solution_2().isNumeric(ss))



# [思路三]：正则表达式（待补。。。）
import re
class Solution_3:
    def isNumeric(self, s):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)

sss = '123e31'
print(Solution_3().isNumeric(sss))