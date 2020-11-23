# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:49:24 2020

@author: wangjingxian
"""

#328. 奇偶链表

'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL


示例 2:
输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL

说明:
	应当保持奇数节点和偶数节点的相对顺序。
	链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

'''


'''
拿到题目之后，第一时间想到的是把链表分成两条：一条奇数，一条偶数，这应该算是最朴素的想法了然后把它们连起来
所以我做了如下操作：
第
一步：头节点肯定是奇数节点，这毋庸置疑。所以odd = head，把头节点拿出来当奇数链表的头节点

第二步：头节点的下一个节点肯定是偶数节点了，所以even = head.next，把 head.next拿出来当偶数链表的头节点，
这里要注意了，一定要把偶数链表的头节点单独拿出来，这里我后面详细说

第三步：找出关系式，奇数链表的下下个节点才会是奇数节点，同样偶数节点的下下个节点才会是偶数节点
odd.next = odd.next.next
even.next = even.next.next

PS:之前做链表题目的时候，.next我经常搞混，但做得多了，我总结了一条经验
‘=’左边的.next一般指的是该节点中存的next（链表节点包括两个部分组成，一个是val，一个是next用于指向下一个部分的），
而右边的.next一般来讲是指的指向的某个具体节点

第四步：找循环终止的条件，什么时候我们可以把所有的节点全部取完？
当odd.next == None or even.next == None时，代表奇数或者偶数已经全部取完了，
剩下的一个会根据它是奇数还是偶数填充到对应链表中
所以循环条件为
while odd.next and even.next:

odd和even链表的头节点进一位
odd,even = odd.next,even.next

第五步：我第二步说的，为什么要把头节点拿出来，因为奇数链表的尾节点要跟偶数链表的头节点相连，从而形成完整的链表
odd.next = even_head

'''

class Solution:
    def oddEvenList(self,head):
        if not head:return head
        odd=head
        even_head=even=head.next
        while odd.next and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd,even=odd.next,even.next
        
        odd.next=even_head
        return head











