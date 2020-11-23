# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:25:18 2020

@author: wangjingxian
"""

#189. 旋转数组
'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]


示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
	尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
	要求使用空间复杂度为 O(1) 的 原地 算法。

'''
#思路一：插入
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())


#思路二：拼接
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

#思路三：三个翻转 ， 整体翻转， 前k翻转，后k翻转
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        #print(nums)
        nums[k:] = nums[k:][::-1]
        #print(nums)


#思路四：模拟过程
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:return 
        start = 0
        tmp = nums[start]
        cnt = 0
        while cnt < n:
            nxt = (start + k) % n
            while nxt != start:
                nums[nxt], tmp = tmp, nums[nxt]
                nxt = (nxt+k) % n
                cnt += 1
            nums[nxt] = tmp
            start += 1
            tmp = nums[start]
            cnt += 1