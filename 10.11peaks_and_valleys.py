# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:28:51 2020

@author: wangjingxian
"""

#面试题 10.11. 峰与谷

'''
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。
例如，在数组{5, 8, 6, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。
示例:
输入: [5, 3, 1, 2, 3]
输出: [5, 1, 3, 2, 3]
提示：
nums.length <= 10000
'''
#排序后将相邻的两个交换

class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(0,len(nums)-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums

#好理解
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums

