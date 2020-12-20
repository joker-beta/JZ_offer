# -*- coding:utf-8 -*-
""" JZ—19  顺时针打印矩阵
题目描述
        输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
        例如，如果输入如下4 X 4矩阵： `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16`
        则依次打印出数字`1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.`
"""

# [思路]：从最外圈按顺时针打印，并在打印完一圈后往内收缩
class Solution:
    def printMatrix(self, matrix):
        rows, columns = len(matrix), len(matrix[0])
        order = []
        # 先固定两个对角顶点，即左上(left, top) 和右下(right, bottom)
        left, right, top, bottom = 0, columns-1, 0, rows-1
        while (left <= right) and (top <= bottom):
            # 1，最上面一行，从左到右添加到 order
            for j in range(left, right+1):
                order.append(matrix[top][j])
            # 2，最右边一列，从上到下添加到 order
            for i in range(top+1, bottom+1):
                order.append(matrix[i][right])
            # 若没有越界，继续添加
            if (left < right) and (top < bottom):
                # 3，最下面一行，从右到左添加到 order
                for j in range(right-1, left, -1):
                     order.append(matrix[bottom][j])
                # 4，最左边一列，从下到上添加
                for i in range(bottom, top, -1):
                    order.append(matrix[i][left])
            # 上面的操作将二维矩阵的最外一层顺时针添加到 order 中
            # 接下来，将定位的两个坐标的网内收缩
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return order

n = 4
m = 5
mat = [[j + i*n for j in range(n)] for i in range(m)]
print(mat)
print(Solution().printMatrix(mat))