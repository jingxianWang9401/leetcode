# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:02:41 2020

@author: wangjingxian
"""

#95. 不同的二叉搜索树 II
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

提示:
	0 <= n <= 8

思路与算法:
二叉搜索树关键的性质是根节点的值大于左子树所有节点的值，小于右子树所有节点的值，且左子树和右子树也同样为二叉搜索树。
因此在生成所有可行的二叉搜索树的时候，假设当前序列长度为 n，如果我们枚举根节点的值为 i，
那么根据二叉搜索树的性质我们可以知道左子树的节点值的集合为 [1…i−1]，右子树的节点值的集合为 [i+1…n]。
而左子树和右子树的生成相较于原问题是一个序列长度缩小的子问题，因此我们可以想到用递归的方法来解决这道题目。

定义 generateTrees(start, end) 函数表示当前值的集合为 [start,end]，返回序列 [start,end]生成的所有可行的二叉搜索树。
按照上文的思路，我们考虑枚举 [start,end]中的值 i为当前二叉搜索树的根，那么序列划分为了 [start,i−1]和 [i+1,end]两部分。
我们递归调用这两部分，即 generateTrees(start, i - 1) 和 generateTrees(i + 1, end)，获得所有可行的左子树和可行的右子树，
那么最后一步我们只要从可行左子树集合中选一棵，再从可行右子树集合中选一棵拼接到根节点上，并将生成的二叉搜索树放入答案数组即可。

递归的入口即为 generateTrees(1, n)，出口为当 start>end时，当前二叉搜索树为空，返回空节点即可。

'''

class Solution:
    def generateTrees(self,n):
        def generateTrees(start, end):
            if start > end:
                return [None,]
            
            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)
                
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            
            return allTrees
        
        return generateTrees(1, n) if n else []




'''
解题思路
二叉搜索树有以下几个特点：

左边的小于当前；
右边的大于当前；
没有重复的值。

为了符合二叉搜索树的这几个特点，我们需要知道当前的范围。（要知道开头和结尾；最开始是1和n）
首先定义一个字典保存已遍历的参数和结果以免重复。
特殊情况判断：如果n == 0，返回[]，如果不判断则会返回[None]（执行递归代码会直接返回，因为0<1）。
递归终止条件：

如果left>right则返回[None]。
以前已经遍历过当前节点则可以直接返回以前的结果。

当前的值可能是left……right，所以我们要把每一个都试一遍，每次循环都要这么做：
递归得到左和右，将返回列表增加它们的全部组合。（值：当前循环变量，左：当前左，右：当前右）
将元组(left，right)作为键，返回列表为值加入字典，然后返回。
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dct = {}

        def left_right(left: int, right: int) -> List[TreeNode]:
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            for i in range(left, right+1):
                left_lst = left_right(left, i-1)
                right_lst = left_right(i+1, right)
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = TreeNode(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret

        return left_right(1, n)
