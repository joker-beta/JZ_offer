# -*- coding:utf-8 -*-
""" JZ—45 扑克牌顺子
题目描述
        一副扑克牌,发现里面居然有 `2` 个大王, `2` 个小王，随机从中抽出了 `5` 张牌，
        看看能不能抽到顺子,大\小 王可以看成任何数字,
        并且 `A` 看作 `1`, `J` 为 `11` , `Q` 为 `12` , `K` 为 `13`，
        使用这幅牌模拟上面的过程， 如果牌能组成顺子就输出 `true`，否则就输出 `false`。
        为了方便起见,你可以认为大小王是 `0`。
"""

# 分情况讨论：假设都排完序
# 1，[1,2,3,4,5], (2-1)+(3-2)+(4-3)+(5-4) = 4   此时满足条件需要相邻元素差累加和 = 4
#    [1,3,4,5,6], (3-1)+(4-3)+(5-4)+(6-5) != 4
# 2，[0,1,2,3,4],
#    [0,0,1,2,3],
#    [0,0,0,1,2]    若0的个数为1-3,那么非零元素相邻差累加和 = 4
# 3，[0,0,0,0,1]    若0的个数为4，必定满足

class Solution:
    def IsContinuous(self, numbers):
        if numbers == []:
            return False
        numbers.sort()
        zero_count = 0
        res = 0
        # 1，若没有0元素
        if 0 not in numbers:
            # 统计相邻差累加和
            for i in range(4):
                res += numbers[i+1] - numbers[i]
            return True if (res == 4) else False
        # 2，若有 0 元素
        else:
            # 若0元素个数为4，或者相邻差累加和为4，返回 True
            if (zero_count == 4) or (res == 4):
                return True
            else:
                return False
