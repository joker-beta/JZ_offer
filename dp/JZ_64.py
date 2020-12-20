# -*- coding:utf-8 -*-
""" JZ—64 滑动窗口的最大值
题目描述：
        给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
        例如，如果输入数组 `{2,3,4,2,6,2,5,1}` 及滑动窗口的大小 `3`，那么一共存在 `6` 个滑动窗口，
        他们的最大值分别为 `{4,4,6,6,6,5}`；

        针对数组 `{2,3,4,2,6,2,5,1}` 的滑动窗口有以下 `6` 个：
        `{[2,3,4],2,6,2,5,1}`，` {2,[3,4,2],6,2,5,1}`， `{2,3,[4,2,6],2,5,1}`，
        `{2,3,4,[2,6,2],5,1}`， `{2,3,4,2,[6,2,5],1}`， `{2,3,4,2,6,[2,5,1]}`。

        窗口大于数组长度的时候，返回空。

例子：
	输入: [2,3,4,2,6,2,5,1],3
	返回值: [4,4,6,6,6,5]
"""

# [思路一]：利用 python 切片策略，每次通过size大小进行窗口移动。
class Solution_1:
    def maxInWindows(self, num, size):
        if (num == []) or (size <= 0):
            return []
        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i:i+size]))
        return res




# [思路二]：模拟窗口移动的过程，
class Solution_2:
    def maxInWindows(self, nums, k):
        # write code here
        if (nums == []) or (k < 0):
            return 0
        left = right = 0
        ans = []   # 存放每个窗口的最大值
        res = []   # 存放每个窗口最大值的下标
        while right < len(nums):
            # 记录当前窗口最大值下标
            # 始终保证res[0]存放当前窗口最大值下标
            while (len(res) > 0) and (nums[res[-1]] <= nums[right]):
                res.pop()
            res.append(right)
            right += 1
            # 若当前窗口长度=k，就将窗口最大值加入ans中，
            while right - left == k:
                ans.append(nums[res[0]])
                # 在进行窗口收缩之前，先判断当前窗口最大值的下标是否是窗口左端点
                # 若是，则将其从res中删除
                if (res[0] == left) and (len(res) > 0):
                    res.pop(0)
                # 然后将窗口收缩
                left += 1
        return ans