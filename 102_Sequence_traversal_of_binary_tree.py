# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:50:42 2020

@author: wangjingxian
"""

#102. 二叉树的层序遍历
'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''

'''
方法一：迭代实现
广度优先遍历是按层层推进的方式，遍历每一层的节点。题目要求的是返回每一层的节点值，所以这题用广度优先来做非常合适。
广度优先需要用队列作为辅助结构，我们先将根节点放到队列中，然后不断遍历队列。

      1
   /     \
  2       5
/  \      \
3   4     6

首先拿出根节点，如果左子树/右子树不为空，就将他们放入队列中。
第一遍处理完后，根节点已经从队列中拿走了，而根节点的两个孩子已放入队列中了，现在队列中就有两个节点 2 和 5。

第二次处理，会将 2 和 5 这两个节点从队列中拿走，然后再将 2 和 5 的子节点放入队列中，现在队列中就有三个节点 3，4，6。

我们把每层遍历到的节点都放入到一个结果集中，最后返回这个结果集就可以了。
时间复杂度： O(n)
空间复杂度：O(n)
'''

class Solution(object):
    def levelOrder(self,root):
        '''
        :type root:TreeNode
        :rtype:List[List[int]]
        
        '''
        if not root:
            return []
        res=[]
        queue=[root]
        while queue:
            #获取当前队列的长度，这个长度相当于当前这一层的节点个数
            size=len(queue)
            tmp=[]
            #将队列中的元素都拿出来（即获取这一层的节点），放到临时list中去
            #如果节点的左/右子树不为空，也放入队列中
            for _ in range(size):
                r=queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)
        return res



'''
方法二：递归实现：用广度优先处理是很直观的，可以想象成是一把刀横着切割了每一层，但是深度优先遍历就不那么直观了。
我们开下脑洞，把这个二叉树的样子调整一下，摆成一个田字形的样子。田字形的每一层就对应一个 list。
      1
   /     \
  2       5
/  \      \
3   4     6

按照深度优先的处理顺序，会先访问节点 1，再访问节点 2，接着是节点 3。
之后是第二列的 4 和 5，最后是第三列的 6。
每次递归的时候都需要带一个 index(表示当前的层数)，也就对应那个田字格子中的第几行，
如果当前行对应的 list 不存在，就加入一个空 list 进去。

时间复杂度：O(N)
空间复杂度：O(h)，h 是树的高度

'''

class Solution(object):
    def levelOrder(self,root):
        if not root:
            return []
        res=[]
        def dfs(index,r):
            #假设res是[ [1],[2,3] ]，index是3，就插入一个空list放到res中
            if len(res)<index:
                res.append([])
            
            #将当前节点的值加入到res中，index代表当前层，假设index是3，节点是99
            #res是[[1],[1,2,3][4]],加入后res变为[[1],[2,3],[4,99]]
            res[index-1].append(r.val)
            #递归的处理左子树，右子树，同时将层数index+1
            if r.left:
                dfs(index+1,r.left)
            if r.right:
                dfs(index+1,r.right)
                
        dfs(1,root)
        return res



































