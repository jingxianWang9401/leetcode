# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:28:37 2020

@author: wangjingxian
"""

#206. 反转链表
'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

'''

'''
方法一：双指针迭代
我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
第二个指针 cur 指向 head，然后不断遍历 cur。
每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。

动画演示中其实省略了一个tmp变量，这个tmp变量会将cur的下一个节点保存起来，考虑到一张动画放太多变量会很混乱，所以我就没加了，
具体详细执行过程，请点击下面的幻灯片查看。
'''

class Solution(object):
    def reverseList(self,head):
        #申请两个节点，pre和cur,pre指向None
        pre=None
        cur=head
        #遍历链表
        while cur:
            #记录当前节点的下一个节点
            tmp=cur.next
            #然后将当前节点指向pre
            cur.next=pre
            #pre和cur节点都前进一位
            pre=cur
            cur=tmp
            
        return pre
    
    
'''
方法二：递归解法
递归的两个条件：

终止条件是当前节点或者下一个节点==null
在函数内部，改变节点的指向，也就是 head 的下一个节点指向 head 递归函数那句

head.next.next = head

很不好理解，其实就是 head 的下一个节点指向head。
递归函数中每次返回的 cur 其实只最后一个节点，在递归函数内部，改变的是当前节点的指向。

'''
class Solution:
    def reverseList(self,head):
        def helper(head):
            if head==None or head.next==None:
                return head,head
            pre,last=helper(head.next)
            last.next=head
            head.next=None
            return pre,head
        rt,_=helper(head)
        return rt
 
    
    
    
    
    
#92. 反转链表 II
'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''        

'''
一、递归反转整个链表
ListNode reverse(ListNode head) {
    if (head.next == null) return head;
    ListNode last = reverse(head.next);
    head.next.next = head;
    head.next = null;
    return last;
}

对于递归算法，最重要的就是明确递归函数的定义。具体来说，我们的 reverse 函数定义是这样的：
输入一个节点 head，将「以 head 为起点」的链表反转，并返回反转之后的头结点。

那么输入 reverse(head) 后，会在这里进行递归：

ListNode last = reverse(head.next);

不要跳进递归（你的脑袋能压几个栈呀？），而是要根据刚才的函数定义，来弄清楚这段代码会产生什么结果：

二、反转链表前 N 个节点
这次我们实现一个这样的函数：
// 将链表的前 n 个节点反转（n <= 链表长度）
ListNode reverseN(ListNode head, int n)

ListNode successor = null; // 后驱节点

// 反转以 head 为起点的 n 个节点，返回新的头结点
ListNode reverseN(ListNode head, int n) {
    if (n == 1) { 
        // 记录第 n + 1 个节点
        successor = head.next;
        return head;
    }
    // 以 head.next 为起点，需要反转前 n - 1 个节点
    ListNode last = reverseN(head.next, n - 1);

    head.next.next = head;
    // 让反转之后的 head 节点和后面的节点连起来
    head.next = successor;
    return last;
}    

具体的区别：
1、base case 变为 n == 1，反转一个元素，就是它本身，同时要记录后驱节点。
2、刚才我们直接把 head.next 设置为 null，因为整个链表反转后原来的 head 变成了整个链表的最后一个节点。
但现在 head 节点在递归反转之后不一定是最后一个节点了，所以要记录后驱 successor（第 n + 1 个节点），
反转之后将 head 连接上。

'''
    
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def reverseN(head,n):
            if n == 1:return head
            last = reverseN(head.next,n-1)
            successor = head.next.next
            head.next.next = head
            head.next = successor
            return last
        if m == 1:return reverseN(head,n)
        head.next = self.reverseBetween(head.next,m-1,n-1)
        return head    
    
    
    
    