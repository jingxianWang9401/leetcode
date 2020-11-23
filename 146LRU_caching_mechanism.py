# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:56:56 2020

@author: wangjingxian
"""

#146. LRU缓存机制

'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

'''

'''
#方法一：面试官不满意的解法
实现本题的两种操作，需要用到一个哈希表和一个双向链表。
在面试中，面试官一般会期望读者能够自己实现一个简单的双向链表，而不是使用语言自带的、封装好的数据结构。
在 Python 语言中，有一种结合了哈希表与双向链表的数据结构 OrderedDict，只需要短短的几行代码就可以完成本题。


OrderedDict有两个重要方法：
popitem(last=True): 返回一个键值对，当last=True时，按照LIFO的顺序，否则按照FIFO的顺序。
move_to_end(key, last=True): 将现有 key 移动到有序字典的任一端。 如果 last 为True（默认）则将元素移至末尾；如果 last 为False则将元素移至开头。
删除数据时，可以使用popitem(last=False)将开头最近未访问的键值对删除。
访问或者设置数据时，使用move_to_end(key, last=True)将键值对移动至末尾。

'''
class LRUCache(collections.OrderedDict):
    def __init__(self,capacity):
        super().__init__()
        self.capacity=capacity
        
    def get(self,key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
    
    def put(self,key,value):
        if key in self:
            self.move_to_end(key)
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)
            
            
'''
方法一：哈希表 + 双向链表算法
LRU 缓存机制可以通过哈希表辅以双向链表实现，我们用一个哈希表和一个双向链表维护所有在缓存中的键值对。
双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。

这样以来，我们首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，
即可在 O(1)时间内完成 get 或者 put 操作。具体的方法如下：


1)对于 get 操作，首先判断 key 是否存在：
如果 key 不存在，则返回 −1；
如果 key 存在，则 key 对应的节点是最近被使用的节点。
通过哈希表定位到该节点在双向链表中的位置，并将其移动到双向链表的头部，最后返回该节点的值。

2)对于 put 操作，首先判断 key 是否存在：
    
如果 key 不存在，使用 key 和 value 创建一个新的节点，在双向链表的头部添加该节点，
并将 key 和该节点添加进哈希表中。然后判断双向链表的节点数是否超出容量，
如果超出容量，则删除双向链表的尾部节点，并删除哈希表中对应的项；

如果 key 存在，则与 get 操作类似，先通过哈希表定位，再将对应的节点的值更新为 value，并将该节点移到双向链表的头部。

上述各项操作中，访问哈希表的时间复杂度为 O(1)，在双向链表的头部添加节点、在双向链表的尾部删除节点的复杂度也为 O(1)。
而将一个节点移到双向链表的头部，可以分成「删除该节点」和「在双向链表的头部添加节点」两步操作，都可以在 O(1)时间内完成。

复杂度分析:

时间复杂度：对于 put 和 get 都是 O(1)。
空间复杂度：O(capacity)，因为哈希表和双向链表最多存储 capacity+1个元素。

'''

class DLinkedNode:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
        
class LRUCache:
    
    def __init__(self,capacity):
        self.cache=dict()
        #使用伪头部和伪尾部节点
        self.head=DLinkedNode()
        self.tail=DLinkedNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.size=0
        
    def get(self,key):
        if key not in self.cache:
            return -1
        #如果key存在，先通过哈希表定位，再移到头部
        node=self.cache[key]
        self.moveToHead(node)
        return node.value
    
    def put(self,key,value):
        if key not in self.cache:
            #如果key不存在，创建一个新的节点
            node=DLinkedNode(key,value)
            #添加进哈希表
            self.cache[key]=node
            #添加至双向链表的头部
            self.addToHead(node)
            self.size+=1
            if self.size>self.capacity:
                #如果超出容量，删除双向链表的尾部节点
                removed=self.removeTail()
                #删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size-=1
        else:
            #如果key存在，先通过哈希表定位，再修改value，并移到头部
            node=self.cache[key]
            node.value=value
            self.moveToHead(node)
            
    def addToHead(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        
    def removeNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)
        
    def removeTail(self):
        node=self.tail.prev
        self.removeNode(node)
        return node
        
    
        
#方法三：            
'''
看到题目要我们实现一个可以存储 key-value 形式数据的数据结构，并且可以记录最近访问的 key 值。
首先想到的就是用字典来存储 key-value 结构，这样对于查找操作时间复杂度就是 O(1)。
但是因为字典本身是无序的，所以我们还需要一个类似于队列的结构来记录访问的先后顺序，这个队列需要支持如下几种操作：

在末尾加入一项
去除最前端一项
将队列中某一项移到末尾

首先考虑列表结构。
对于列表加入有 append()，删除有 pop() 操作，这两个都是 O(1)的时间复杂度。而对于将队列中某一项移到末尾，
因为列表中存储的是哈希表的 key，考虑这样一种情况：
# 操作
cache = LRUCache(4)
cache.put(3, 2)
cache.put(2, 1)
cache.put(1, 1)
# 操作之后队列：
# queue = [3, 2, 1]

此时我们再进行 cache.put(2, 2) 的操作，因为2已经存在在哈希表中，这说明队列中已经存在值为2的元素，那么问题来了，
如何在常数时间内把它挑出来移到队尾呢？
答案是不行，所以用列表无法实现常熟时间复杂度。
之后再考虑单链表。
对于单链表，哈希表的结构类似于 {key: ListNode(value)}，即键所对应的是一个节点地址，节点的值是 value。
对于链表，遇到上面那种情况时可以在常数的时间内找到对应的节点，但是如果想将它移到尾部则需要从头遍历到该节点才能保证链表不断，对于这种情况需要的时间复杂度也是O(n)O(n)O(n)
为了解决移到末尾这个问题，需要使用双链表来记录，结构大概如下图所示：
'''

     
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_tail(self, key):
            # 先将哈希表key指向的节点拎出来，为了简洁起名node
            #      hashmap[key]                               hashmap[key]
            #           |                                          |
            #           V              -->                         V
            # prev <-> node <-> next         pre <-> next   ...   node
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 之后将node插入到尾节点前
            #                 hashmap[key]                 hashmap[key]
            #                      |                            |
            #                      V        -->                 V
            # prev <-> tail  ...  node                prev <-> node <-> tail
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new

