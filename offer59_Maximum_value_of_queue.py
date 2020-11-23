# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:33:25 2020

@author: wangjingxian
"""

#剑指 Offer 59 - II. 队列的最大值

'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]


示例 2：
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
'''

'''
方法一：暴力
直接实现一个普通的队列，查询最大值时遍历计算。
'''
import queue
class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1



'''
方法二：维护一个单调的双端队列


应用程序接口（Application Programming Interface，API）是一些预先定义的函数，或指软件系统不同组成部分衔接的约定。

调用 API 函数就像雇佣一位维修工，我们不需要了解维修工是如何修好灯泡的🌚，我们只关心最终灯泡能不能亮🌝。
本题中 max_value、push_back、pop_front 就是一些 API 函数，我们需要来设计这些函数以供他人直接调用，
并且调用每个函数时，时间复杂度均为 O(1)。

思路：
1、对于一个普通队列，push_back 和 pop_front 的时间复杂度都是 O(1)，因此我们直接使用队列的相关操作就可以实现这两个函数。
对于 max_value 函数，我们通常会这样思考，即每次入队操作时都更新最大值：
但是当出队时，这个方法会造成信息丢失，即当最大值出队后，我们无法知道队列里的下一个最大值。

2、为了解决上述问题，我们只需记住当前最大值出队后，队列里的下一个最大值即可。
具体方法是使用一个双端队列 deque，在每次入队时，如果 deque队尾元素小于即将入队的元素value，
则将小于value的元素全部出队后，再将 valuevaluevalue 入队；否则直接入队。

这时，辅助队列 deque队首元素就是队列的最大值。
'''

import queue
class MaxQueue:
    """1队列+1双端队列"""
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
        # return self.deque[0] if self.deque else -1 或者这样写

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)
        

    def pop_front(self) -> int:
        if not self.deque: return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

