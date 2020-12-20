# -*- coding:utf-8 -*-
""" JZ-31 整数中 1 出现的次数

题目描述：求出 `1~13` 的整数中 `1` 出现的次数,并算出 `100~1300` 的整数中 `1` 出现的次数？
        为此他特别数了一下 `1~13` 中包含 `1` 的数字有 `1、10、11、12、13` 因此共出现 `6` 次,
        但是对于后面问题他就没辙了。`ACMer` 希望你们帮帮他,并把问题更加普遍化,
        可以很快的求出任意非负整数区间中 `1` 出现的次数（从 `1` 到 `n` 中 `1` 出现的次数）。
"""

# 方法一：调用内置函数 arr.count(str) 计算arr中字符(串)str 出现的次数
class Solution_1:
    def NumberOf1Betetween1AndN_Solution(self, n):
        if (n < 1):
            return 0
        count = 0
        for i in range(1, n+1):
            count += self.Count(i)
        return count

    def Count(self, m):
        """计算数字m中数码'1'的个数"""
        arr = list(str(m))   # 将数字 m 转为字符列表
        return arr.count('1')   # 再返回列表中 '1' 的个数




# 方法二：(待补。。。)
class Solution_2:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if (n < 1):
            return 0
        Len = self.getLen(n)  # 获得整数长度
        if (Len == 1):
            return 1

        tmp1 = pow(10, Len - 1)
        first = n // tmp1  # 获得整数的首位数字
        if first == 1:  # 若首位数字为1
            firstnum = n % tmp1 + 1
        else:  # 若首位数字不为1
            firstnum = tmp1
        othernum = first * (Len - 1) * (tmp1 // 10)
        return firstnum + othernum + self.NumberOf1Between1AndN_Solution(n % tmp1)

    def getLen(self, n):
        """计算整数的位数长度"""
        Len = 0
        while (n != 0):
            Len += 1
            n = n // 10
        return Len
