""" JZ_66 机器人的运动范围

题目描述：地上有一个 m行和 m 列的方格。一个机器人从坐标 (0,0) 的格子开始移动，
        每一次只能向左，右，上，下四个方向移动一格，
        但是不能进入行坐标和列坐标的数位之和大于 k 的格子。

        例如，当 k 为 18 时，机器人能够进入方格 (35,37)，因为 3+5+3+7 = 18。
        但是，它不能进入方格 (35,38)，因为 3+5+3+8 = 19。请问该机器人能够达到多少个格子 ?
"""
import sys

# 添加下面代码，重新定义最大递归深度
sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
# 否则出现报错：
# RecursionError: maximum recursion depth exceeded while getting the str of an object


class Solution:
    def movingCount(self, k, rows, cols):
        self.count = 0   # 统计能达到的格子数
        arr = [[1 for j in range(cols)] for i in range(rows)]
        # 从 (0,0) 开始遍历
        self.findway(arr, 0, 0, k)
        return self.count

    def findway(self, arr, i, j, k):
        # 越界直接返回
        if (i < 0 or j < 0) or (i >= len(arr) or j >= len(arr[0])):
            return

        # 为了要计算各数码的累加和，所以将横纵坐标数码转为数组
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))

        # 1，若不满足累加和要求，或者当前点已经遍历过，直接返回
        if (sum(tmpi) + sum(tmpj) > k) or (arr[i][j] != 1):
            return

        # 2，若满足累加和要求，进行遍历
        # 首先，将当前点标记为0，表示已经遍历过
        arr[i][j] = 0
        self.count += 1  # 找到一个满足要求的点，将个数更新
        # 然后，基于当前点分别往上下左右遍历
        self.findway(arr, i+1, j, k)  # 左
        self.findway(arr, i-1, j, k)  # 右
        self.findway(arr, i, j+1, k)  # 上
        self.findway(arr, i, j-1, k)  # 下


k = 30
rows = 50
cols = 50
print(Solution().movingCount(k, rows, cols))