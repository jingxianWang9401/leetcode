# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:27:00 2020

@author: wangjingxian
"""

#704. 二分查找

'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4


示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

	你可以假设 nums 中的所有元素是不重复的。
	n 将在 [1, 10000]之间。
	nums 的每个元素都将在 [-9999, 9999]之间。

'''

'''
方法：二分查找
二分查找是一种基于比较目标值和数组中间元素的教科书式算法。

如果目标值等于中间元素，则找到目标值。
如果目标值较小，继续在左侧搜索。
如果目标值较大，则继续在右侧搜索。

算法：

初始化指针 left = 0, right = n - 1。
当 left <= right：

比较中间元素 nums[pivot] 和目标值 target 。

     如果 target = nums[pivot]，返回 pivot。
     如果 target < nums[pivot]，则在左侧继续搜索 right = pivot - 1。
     如果 target > nums[pivot]，则在右侧继续搜索 left = pivot + 1。

'''

class Solution:
    def search(self,nums):
        left,right=0,len(nums)-1
        while left<=right:
            pivot=left+(right-left)//2
            if nums[pivot]==target:
                return pivot
            if target <nums[pivot]:
                right=pivot-1
            else:
                left=pivot+1
                
        return -1














