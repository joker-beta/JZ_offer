# -*- coding:utf-8 -*-
"""
题目描述
        把只包含质因子 `2、3` 和 `5` 的数称作丑数（Ugly Number）。
        例如： `6、8` 都是丑数，但 `14` 不是，因为它包含质因子 `7`。
        习惯上我们把 `1` 当做是第一个丑数。求按从小到大的顺序的第 `N` 个丑数。
"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        # 1，若序号为空，直接返回0
        if index <= 0:
            return 0

        # 2，若序号不为空，则通过索引判断是否为丑数
        res = [1]
        # 设置质因子2，3，5的统计下标
        index2 = index3 = index5 = 0
        for i in range(1, index):
            u2 = res[index2] * 2
            u3 = res[index3] * 3
            u5 = res[index5] * 5
            res.append(min(u2, u3, u5))   # res 中的数按照顺序排序，所以每次添加当前比较的最小值

            # 2.1，若当前遍历下标对应的数能被2整除，说明该数包含2因子，则将前一个index2更新
            if res[i]//2 == res[index2]:
                index2 += 1
            # 2.2，若当前遍历下标对应的数能被3整除，说明该数包含3因子，则将前一个index3更新
            if res[i]//3 == res[index3]:
                index3 += 1
            # 2.3，若当前遍历下标对应的数能被5整除，说明该数包含5因子，则将前一个index5更新
            if res[i]//5 == res[index5]:
                index5 += 1

        return res[-1]

index = 100
print(Solution().GetUglyNumber_Solution(index))