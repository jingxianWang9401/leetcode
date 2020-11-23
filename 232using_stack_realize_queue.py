# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:22:57 2020

@author: wangjingxian
"""

#232. 用栈实现队列

'''
使用栈实现队列的下列操作：

	push(x) -- 将一个元素放入队列的尾部。
	pop() -- 从队列首部移除元素。
	peek() -- 返回队列首部的元素。
	empty() -- 返回队列是否为空。

示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false


说明:


	你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
	你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
	假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

'''



'''

因为python没有栈的数据结构，所以我们用list来模拟栈操作，append操作代表栈顶加入元素，pop操作代表弹出栈顶元素，
此外还可以使用len函数计算栈的元素个数，其他的列表操作均不可以使用！
（1）初始化两个栈结构，stack1为主栈，stack2为辅助栈
（2）push往stack1末尾添加元素，利用append即可实现
（3）pop时候，先将stack1元素向stack2转移，知道stack1只剩下一个元素时候（这就是我们要返回的队列首部元素），
然后我们再把stack2中的元素转移回stack1中即可
（4）类似于步骤（3）的操作，唯一不同是这里我们需要将elenment先添加回stack2，
然后再将stack2的元素转移回stack1中，因为peek操作不需要删除队列首部元素
（5）empty判断stack1尺寸即可

'''



     class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []     # 主栈
        self.stack2 = []     # 辅助栈

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        element = self.stack1.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return element

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        element = self.stack1.pop()
        self.stack2.append(element)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

        
        
        
        
        
        
        
        
        