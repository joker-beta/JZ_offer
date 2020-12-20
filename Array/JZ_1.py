# -*- coding:utf-8 -*-
""" JZ—1 二维数组中的查找
题目描述：
        在一个二维数组中（每个一维数组的长度相同），
        每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例1
	输入 7,	  [[1, 2, 8, 9],
			   [2, 4, 9, 12],
			   [4, 7, 10, 13],
			   [6, 8, 11, 15]]
	返回值 true
"""

# 思路：类似二分查找的策略，记当前遍历元素为cur,目标元素为tar，初始位置第一行最后一列的位置。
# 	1，若cur < tar[行][列]，则 列-1
# 	2，若cur > tar[行][列]，则 行+1
# 	3，若cur = tar[行][列]，则返回。
class Solution:
    def Find(self, target, array):
        rows = len(array)
        cols = len(array[0])
        if (rows > 0) and (cols > 0):
            # 选取数组右上角元素为初始元素，开始对比
            row = 0  # 第一行
            col = cols - 1  # 最后一列
            while (row < rows) and (col >= 0):
                if target == array[row][col]:
                    return True
                # 若目标值比当前遍历大，说明应该在下一行开始查找
                elif target > array[row][col]:
                    row += 1
                # 若目标值比当前遍历值小，说明应该在当前列的左边进行查找
                elif target < array[row][col]:
                    col -= 1
            # 若遍历完整个数组，还是没有找到，说明数组中不存在该值
            return False


mat = [[1, 2, 8, 9],
       [2, 4, 9, 12],
       [4, 7, 10, 13],
       [6, 8, 11, 15]]
target = 6
print(Solution().Find(target, mat))