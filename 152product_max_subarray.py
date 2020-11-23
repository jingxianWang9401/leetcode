# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:08:50 2020

@author: wangjingxian
"""

#152. 乘积最大子数组
'''
给你一个整数数组nums,请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。


思路：动态规划
我们只要记录前i的最小值, 和最大值, 那么 dp[i] = max(nums[i] * pre_max, nums[i] * pre_min, nums[i]), 
这里0 不需要单独考虑, 因为当相乘不管最大值和最小值,都会置0
'''

class Solution:
    def maxProduct(self,nums):
        if not nums:
            return
        res=nums[0]
        pre_max=nums[0]
        pre_min=nums[0]
        for num in nums[1:]:
            cur_max=max(pre_max*num,pre_min*num,num)
            cur_min=min(pre_max*num,pre_min*num,num)
            res=max(res,cur_max)
            pre_max=cur_max
            pre_min=cur_min
        return res