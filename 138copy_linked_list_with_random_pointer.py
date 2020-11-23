# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:32:07 2020

@author: wangjingxian
"""

#leetcode138 复制带随机指针的链表

'''
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的 深拷贝。 
我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
	val：一个表示 Node.val 的整数。
	random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
'''


'''
方法 1：回溯

想法:
回溯算法的第一想法是将链表想象成一张图。链表中每个节点都有 2 个指针（图中的边）。因为随机指针给图结构添加了随机性，
所以我们可能会访问相同的节点多次，这样就形成了环。

上图中，我们可以看到随机指针指向了前一个节点，因此成环。我们需要考虑这种环的实现。
此方法中，我们只需要遍历整个图并拷贝它。拷贝的意思是每当遇到一个新的未访问过的节点，你都需要创造一个新的节点。
遍历按照深度优先进行。我们需要在回溯的过程中记录已经访问过的节点，否则因为随机指针的存在我们可能会产生死循环。

算法
1、从头指针开始遍历整个图。
我们将链表看做一张图。下图对应的是上面的有向链表的例子，Head 是图的出发节点。
2、当我们遍历到某个点时，如果我们已经有了当前节点的一个拷贝，我们不需要重复进行拷贝。
3、如果我们还没拷贝过当前节点，我们创造一个新的节点，并把该节点放到已访问字典中，即：
visited_dictionary[current_node] = cloned_node_for_current_node.
4、我们针对两种情况进行回溯调用：一个顺着 random 指针调用，另一个沿着 next 指针调用。
步骤 1 中将 random 和 next 指针分别红红色和蓝色标注。然后我们分别对两个指针进行函数递归调用：

cloned_node_for_current_node.next=copyRandomList(current_node.next)
cloned_node_for_current_node.random=copyRandomList(current_node.random)

复杂度分析

时间复杂度：O(N) ，其中 NNN 是链表中节点的数目。
空间复杂度：O(N)。如果我们仔细分析，我们需要维护一个回溯的栈，同时也需要记录已经被深拷贝过的节点，也就是维护一个已访问字典。渐进时间复杂度为 O(N)O(N)O(N) 。

'''

class Solution(object):
    def __init__(self):
        self.visitedHash={}
        
    def copyRandomList(self,head):
        if head==None:
            return None
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        node=Node(head.val,None,None)
        
        self.visitedHash[head]=node

        node.next=self.copyRandomList(head.next)
        node.random=self.copyRandomList(head.random)
        
        return node















