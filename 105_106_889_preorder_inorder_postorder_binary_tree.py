# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:10:57 2020

@author: wangjingxian
"""
#1、根据一棵树的前序遍历与中序遍历构造二叉树。
'''
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


前序遍历：遍历顺序为 父节点 -> 左子节点 -> 右子节点
后续遍历：遍历顺序为 左子节点 -> 父节点 -> 右子节点
构建二叉树的问题本质上就是：
找到各个子树的根节点 root
构建该根节点的左子树
构建该根节点的右子树
整个过程可以用递归来完成。
'''
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def buildTree(self,preorder,inorder):
        '''
        input:
            preorder:list[int],inorder:list[int]
        output:
            TreeNode   
        '''
        if len(inorder)==0:
            return None
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:1+mid],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
#时间复杂度：O（n^2)
        
    
 

#2、根据一棵树的中序遍历与后序遍历构造二叉树。
'''
注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

与从前序与中序遍历序列构造二叉树完全一致
后序遍历是左右根，因此postorder最后一个元素一定整个树的根。由于题目说明了没有重复元素，因此我们可以通过val去inorder找到根在inorder中的索引i。
而由于中序遍历是左根右，我们容易找到i左边的都是左子树，i右边都是右子树。

'''
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

    
class Solution(object):
    def buildTree(self,inorder,postorder):
        '''
        input:
            inorder:list[int],postorder:list[int]
        output:
            TreeNode   
        '''
        if len(inorder)==0:
            return None
        root=TreeNode(postorder[-1])
        mid=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[:mid],postorder[:mid])
        root.right=self.buildTree(inorder[mid+1:],postorder[mid:-1])
        return root





#3、根据前序和后序遍历构造二叉树
'''
返回与给定的前序和后序遍历匹配的任何二叉树。
 pre 和 post 遍历中的值是不同的正整数。
 
示例：
输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 
 
               1
               
        2           3
          
   4       5    6      7
   
前序遍历的结果是[1,2,4,5,3,6,7]
后序遍历的结果是[4,5,2,6,7,3,1]
前序遍历的特点是根节点始终出现在第一位
后序遍历的特点是根节点始终出现在最后一位

前序遍历第一个元素是根节点[1]，后面的那一堆就是左子树[2,4,5]，接着是右子树[3,6,7]
而后序遍历第一个出现的是左子树[4,5,2]，然后是右子树[3,6,7]，最后才是根节点[1]
如果遍历这个左子树
前序遍历的结果是[2,4,5]
后序遍历的结果是[4,5,2]
我们根据2就可以确定出后序遍历的左子树范围
现在我们找到2了，根节点的位置是固定出现在最后的，那么右子树的范围也就可以确定了。
后序遍历数组下标是从0开始的，我们确定了2的位置，还需要+1，这样就得到了整个左子树的个数。

拆分的前序数组：

左半部分[1,left_count+1)
右半部分[left_count+1,N)

拆分的后序数组：

左半部分[0,left_count)
右半部分[left_count,N-1)

'''


#Definition for a binary tree node.
class TreeNode: 
    def __init__(self, x):        
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre)==0:
            return None
        # 根据前序数组的第一个元素，创建根节点
        root = TreeNode(pre[0])
        # 数组长度为1时，直接返回即可
        if len(pre) == 1: 
            return root
        # 根据前序数组第二个元素，确定后序数组左子树范围
        L = post.index(pre[1]) + 1
        # 递归执行前序数组左边、后序数组左边
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        # 递归执行前序数组右边、后序数组右边
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        # 返回根节点
        return root







