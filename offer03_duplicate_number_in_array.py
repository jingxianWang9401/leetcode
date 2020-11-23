# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:20:10 2020

@author: wangjingxian
"""

#剑指 Offer 03. 数组中重复的数字
'''
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

'''




#方法一：利用集合（set)的无序不重复特性，通过判断temp_set的长度确定是否是重复数字
class Solution:
    def findRepeatNumber(self,nums):
        temp_set=set()
        repeat=-1
        for i in range(len(nums)):
            temp_set.add(nums[i])
            if len(temp_set)<i+1:
                repeat=nums[i]
                break
        return repeat
    

#方法二：利用python的sort函数排序，然后计算相邻两个数据是否相等即可。
class Solution:
    def findRepeatNumber(self,nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]