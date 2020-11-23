# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:25:55 2020

@author: wangjingxian
"""

#669. 修剪二叉搜索树

'''
给定一个二叉搜索树，同时给定最小边界L和最大边界R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例 1:

输入: 
    1
   / \
  0   2

  L = 1
  R = 2

输出: 
    1
      \
       2


示例 2:

输入: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

输出: 
      3
     / 
   2   
  /
 1


'''


'''
方法：递归
思路
令 trim(node) 作为该节点上的子树的理想答案。我们可以递归地构建该答案。

算法
当 node.val > R，那么修剪后的二叉树必定出现在节点的左边。
类似地，当 node.val < L，那么修剪后的二叉树出现在节点的右边。否则，我们将会修剪树的两边。

复杂度分析:

时间复杂度：O(N)，其中 N是给定的树的全部节点。我们最多访问每个节点一次。
空间复杂度：O(N)，即使我们没有明确使用任何额外的内存，在最糟糕的情况下，我们递归调用的栈可能与节点数一样大。
'''

class Solution(object):
    def trimBST(self,root,L,R):
        def trim(node):
            if not node:
                return None
            elif node.val>R:
                return trim(node.left)
            elif node.val<L:
                return trim(node.right)
            else:
                node.left=trim(node.left)
                node.right=trim(node.right)
                
                return node
            
        return trim(root)
    
    
    


'''
递归，前序遍历
解题思路
判断越界后的返回值
右边越界，返回左边节点
左边越界，返回右边节点

'''

class Solution:
    def trimBST(self,root,L,R):
        if not root:
            return 
        if root.val>R:
            return self.trimBST(root.left,L,R)
        if root.val<L:
            return self.trimBST(root.right,L,R)
        else:
            root.left=self.trimBST(root.left,L,R)
            root.right=self.trimBST(root.right,L,R)
            return root


























