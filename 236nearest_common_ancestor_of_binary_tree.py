# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:56:35 2020

@author: wangjingxian
"""

#236. 二叉树的最近公共祖先
'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

                        3
                      /   \
                     5     1
                    / \   / \
                   6   2  0  8
                      /\
                     7  4

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。


示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


说明:
	所有节点的值都是唯一的。
	p、q 为不同节点且均存在于给定的二叉树中。


'''

'''
解题思路：
祖先的定义： 若节点 p在节点 root的左（右）子树中，或 p=root，则称 root是 p的祖先。

             3
           /  \
          5    1
         / \  / \
        6  2 0  8
          /\
         7 4
节点7的公共祖先有：3、5、2、7
最近公共祖先的定义： 设节点 root为节点 p,q的某公共祖先，若其左子节点 root.left和右子节点 root.right都不是 p,q的公共祖先，
则称 root是 “最近的公共祖先” 。

根据以上定义，若 root是 p,q的最近公共祖先 ，则只可能为以下情况之一：

1）p和 q在 root的子树中，且分列 root的 异侧（即分别在左、右子树中）；
2）p=root，且 q在 root的左或右子树中；
3）q=root，且 p在 root的左或右子树中；

考虑通过递归对二叉树进行后序遍历，当遇到节点 p或 q时返回。从底至顶回溯，当节点 p,q在节点 root的异侧时，
节点 root即为最近公共祖先，则向上返回 root 。

递归解析：

1、终止条件：
当越过叶节点，则直接返回 null；
当 root等于p,q，则直接返回 root；

2、递推工作： 
开启递归左子节点，返回值记为 left ；
开启递归右子节点，返回值记为 right；

3、返回值： 根据 left和 right，可展开为四种情况；

1）当 left和 right同时为空 ：说明 root的左/右子树中都不包含 p,q，返回 null ；
2）当 left和 right同时不为空 ：说明 p,q分列在 root的 异侧 （分别在 左 / 右子树），因此 root为最近公共祖先，
返回 root；

3）当 left为空 ，right不为空 ：p,q都不在 root的左子树中，直接返回 right。具体可分为两种情况：

a)p,q其中一个在 root的右子树中，此时 right指向 p（假设为 p）；
b)p,q两节点都在 root的右子树中，此时的 right指向最近公共祖先节点 ；

4)当 left不为空 ， right为空 ：与情况 3. 同理；

    观察发现， 情况 1. 可合并至 3. 和 4. 内，详见文章末尾代码。
    
复杂度分析：

时间复杂度 O(N)： 其中 N为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度 O(N)： 最差情况下，递归深度达到 N，系统使用 O(N)大小的额外空间。 
    
'''

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        if not root or root==p or root==q: return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root 



#将1）2）3）4）展开写法如下：
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return # 1.
        if not left: return right # 3.
        if not right: return left # 4.
        return root # 2. if left and right:













