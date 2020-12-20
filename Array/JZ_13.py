# -*- coding:utf-8 -*-
"""
题目描述
        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
        所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# [思路一]：冒泡排序的想法，若相邻两项偶数出现在奇数前面，则交换
class Solution_1:
    def reOrderArray(self, array):
        n = len(array)
        for i in range(n):
            for j in range(1, n-i):
                # 若相邻两项，偶数出现在奇数前面，则交换
                if (array[j-1]%2 == 0) and (array[j]%2 == 1):
                    array[j-1], array[j] = array[j], array[j-1]
        return array

arr = [i for i in range(10)]
print(Solution_1().reOrderArray(arr))



# [思路二]：将奇数偶数分别存到两个列表中，最后再合并
class Solution_2:
    def reOrderArray(self, array):
        odd = []  # 存放奇数
        even = []  # 存放偶数
        for i in range(len(array)):
            if array[i]%2 == 1:
                odd.append(array[i])
            else:
                even.append(array[i])
        return odd + even

    
arr2 = [3*i+2 for i in range(10)]
print(Solution_2().reOrderArray(arr2))