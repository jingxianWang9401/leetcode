# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:22:44 2020

@author: wangjingxian
"""

#234. 回文链表
'''
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

'''

'''
方法一：将值复制到数组中后用双指针法
算法：
我们可以分为两个步骤：

复制链表值到数组列表中。
使用双指针法判断是否为回文。

第一步，我们需要遍历链表将值复制到数组列表中。我们用 currentNode 指向当前节点。每次迭代向数组添加 currentNode.val，
并更新 currentNode = currentNode.next，当 currentNode = null 则停止循环。
执行第二部的最佳方法取决于你使用的变成语言。在 Python 中，很容易构造一个列表的反向副本，也很容易比较两个列表。
在其他语言中，就没有那么简单。因此最好使用双指针法来检查是否为回文。我们在起点放置一个指针，在结尾放置一个指针，
每一次迭代判断两个指针指向的元素是否相同，若不同，返回 false；相同则将两个指针向内移动，并继续判断，直到相遇。
在编码的过程中，注意我们比较的是节点值的大小，而不是节点本身。正确的比较方式是：node_1.val==node_2.val。
而 node_1==node_2 是错误的。

复杂度分析

时间复杂度：O(n)，其中 n指的是链表的元素个数。

第一步： 遍历链表并将值复制到数组中，O(n)。
第二步：双指针判断是否为回文，执行了 O(n/2) 次的判断，即 O(n)。
总的时间复杂度：O(2n)=O(n)。

空间复杂度：O(n)，其中 n指的是链表的元素个数，我们使用了一个数组列表存放链表的元素值。

'''

def isPalindrome(self,head):
    vals=[]
    current_node=head
    while current_node is not None:
        vals.append(current_node.val)
        current_node=current_node.next
    return vals==vals[::-1]
















