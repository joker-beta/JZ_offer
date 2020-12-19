""" JZ—23 字符串的排列
题目描述：输入一个字符串，按字典序打印出该字符串中字符的所有排列。
        例如输入字符串 `abc`，则按字典序打印出由字符 `a, b, c`
        所能排列出来的所有字符串 `abc, acb, bac, bca, cab` 和 `cba`。

例子：
    输入："ab"
    输出：["ab", "ba"]
"""

class Solution:
    def Permutation(self, Str):
        if len(Str) == 0:
            return []
        if len(Str) == 1:
            return [Str]
        # 创建一个集合用于去除重复字符串
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取 a,b,c...全部渠道
        # 然后递归求解
        for i in range(len(Str)):
            # 对Str中除去Str[i]元素外余下的字符串构成的所有排列进行遍历
            # 此时，将Str[i] 作为新字符串的首字符进行拼接，构成新的字符排序
            for j in self.Permutation(Str[:i] + Str[i+1:]):
                res.add(Str[i] + j)    # set() 集合添加元素的方法 add()
        # 每次添加完之后进行字典排序，再返回
        return sorted(res)

strs ='abc'
print(Solution().Permutation(strs))


