# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:20:57 2020

@author: wangjingxian
"""

#114. 二叉树展开为链表

'''
给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6

将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''


'''
方法一：前序遍历
将二叉树展开为单链表之后，单链表中的节点顺序即为二叉树的前序遍历访问各节点的顺序。
因此，可以对二叉树进行前序遍历，获得各节点被访问到的顺序。
由于将二叉树展开为链表之后会破坏二叉树的结构，因此在前序遍历结束之后更新每个节点的左右子节点的信息，将二叉树展开为单链表。

'''

class Solution:
    def flatten(self,root):
        preorderList=list()
        
        def preorderTraversal(root):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
                
        preorderTraversal(root)
        size=len(preorderList)
        
        for i in range(1,size):
            prev,curr=preorderList[i-1],preorderList[i]
            prev.left=None
            prev.right=curr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        