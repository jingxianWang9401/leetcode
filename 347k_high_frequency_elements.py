# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:21:10 2020

@author: wangjingxian
"""

#347. 前 K 个高频元素(没有懂，后续需要继续研究学习)

#给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

'''
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
	你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
	你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
	题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
	你可以按任意顺序返回答案。
'''

'''
解题思路：
更新 0623： 更新为位操作，占位节点版本，简化的代码，方便记忆。
这题是对 堆，优先队列  很好的练习，因此有必要自己用python实现研究一下。堆 处理海量数据的 topK，分位数 非常合适，
优先队列 应用在元素优先级排序，比如本题的频率排序非常合适。与基于比较的排序算法 时间复杂度 O(nlogn)相比，
使用 堆，优先队列 复杂度可以下降到 O(nlogk)，在总体数据规模 n 较大，而维护规模 k 较小时，时间复杂度优化明显。
堆，优先队列 的本质其实就是个完全二叉树，有其下重要性质
ps: 堆 heap[0] 插入一个占位节点，此时堆顶为 index 为 1 的位置，可以更方便的运用位操作。
[1,2,3] -> [0,1,2,3]

父节点 index 为 i
左子节点 index 为 i << 1
右子节点 index 为 i << 1 | 1
大顶堆中每个父节点大于子节点，小顶堆每个父节点小于子节点
优先队列以优先级为堆的排序依据
因为性质 1，2，3，堆可以用数组直接来表示，不需要通过链表建树。

堆，优先队列 有两个重要操作，时间复杂度均是 O(logk)。以小顶锥为例：

上浮 sift up: 向堆尾新加入一个元素，堆规模 +1，依次向上与父节点比较，如小于父节点就交换。
下沉 sift down: 从堆顶取出一个元素（堆规模 -1，用于堆排序）或者更新堆中一个元素（本题），
依次向下与子节点比较，如大于子节点就交换。

对于 topk 问题：最大堆求topk小，最小堆求 topk 大。

topk小：构建一个 k 个数的最大堆，当读取的数小于根节点时，替换根节点，重新塑造最大堆
topk大：构建一个 k 个数的最小堆，当读取的数大于根节点时，替换根节点，重新塑造最小堆

这一题的总体思路 总体时间复杂度 O(nlogk)

遍历统计元素出现频率 O(n)
前k个数构造 规模为 k+1 的最小堆 minheap， O(k)， 注意 +1 是因为占位节点。
遍历规模k之外的数据，大于堆顶则入堆，下沉维护规模为k的最小堆 minheap. O(nlogk)
(如需按频率输出，对规模为k的堆进行排序)

'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就一直下沉"""
            val = arr[root] # 用类似插入排序的赋值交换
            while root<<1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            """上浮log(k),如果新加入的节点<父节点就一直上浮"""
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0,0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1) 
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1) 
        return [item[0] for item in heap[1:]]



'''
方法二：
使用计数器之后构建最小堆
堆的元素可以是元组类型
因为求前 K 个高频元素，python 默认最小堆，则将频次取负再入堆
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #collections：高性能容量数据类型。Counter：计数器，常用于统计的一种数据类型
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))#heapq.heappush(heap, item)，将item添加到堆中, 保留堆条件。 Python中的heapq模块提供了一种堆队列heapq类型,这样实现堆排序等算法便相当方便
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
            #heapq.heappush(heap, item)：将元素添加到heap中
            #heapq.heappop(heap)：返回 root 节点，即 heap 中最小的元素
        return ans






