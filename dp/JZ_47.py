# -*- coding:utf-8 -*-
""" JZ—47 礼物的最大价值
题目描述
        在一个 `mxn` 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 `0`）。
        你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
        给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

例子
	输入: [[1,3,1],
		   [1,5,1],
		   [4,2,1]]
	返回值: 12
	解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""

from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # dp[i][j] 表示走到 grid[i][j]位置时，获得的最大收益
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        # 1，先计算dp矩阵第一列的元素
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # 2，再计算dp矩阵第一行的元素
        for j in range(1, len(grid[0])):
            dp[0][j] =dp[0][j-1] + grid[0][j]
        # 3，最后再计算dp矩阵内部元素
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]