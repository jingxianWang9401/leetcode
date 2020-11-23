# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:07:57 2020

@author: wangjingxian
"""

#300. 最长上升子序列,这道题当初没看懂
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
	可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
	你算法的时间复杂度应该为 O(n^2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

'''
方法一：动态规划
子序列的问题->动态规划。

使用数组 cell 保存每步子问题的最优解。
cell[i] 代表含第 i 个元素的最长上升子序列的长度。
求解 cell[i] 时，向前遍历找出比 i 元素小的元素 j，令 cell[i] 为 max（cell[i],cell[j]+1)。
'''
class Solution:
    def lengthOfLIS(self,nums):
        if nums==[]:
            return 0
        cell=[1]
        for i in range(1,len(nums)):
            cell.append(1)
            for j in range(i):
                if(nums[j]<nums[i]):
                    cell[i]=max(cell[i],cell[j]+1)
        return max(cell)
    
#时间复杂度：O(n^2),双层遍历.空间复杂度：O(n)
        
'''
方法二：动态规划+二分查找
很具小巧思。新建数组 cell，用于保存最长上升子序列。
对原序列进行遍历，将每位元素二分插入 cell 中。

如果 cell 中元素都比它小，将它插到最后
否则，用它覆盖掉比它大的元素中最小的那个。

总之，思想就是让 cell 中存储比较小的元素。这样，cell 未必是真实的最长上升子序列，但长度是对的。
'''

class Solution:
    def lengthOfLIS(self,nums):
        size = len(nums)
        if size<2:
            return size
        
        cell = [nums[0]]
        for num in nums[1:]:
            if num>cell[-1]:
                cell.append(num)
                continue
            
            l,r = 0,len(cell)-1
            while l<r:
                mid = l + (r - l) // 2
                if cell[mid]<num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num
        return len(cell)

