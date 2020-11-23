# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 09:07:42 2020

@author: wangjingxian
"""

#217. 存在重复元素 
'''
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

#注意字典的使用；
#dic[key]与dic.get(key)的区别，后者可以有效避免在key不存在时的情况，
#前者会报错keyerror。
'''

class Solution:
    def containDuplicate(self,nums):
        dic={}
        for num in nums:
            if dic.get(num):
                return True
            dic[num]=1
            
        return False



 
#219. 存在重复元素 II
'''
给定一个整数数组和一个整数k，判断数组中是否存在两个不同的索引i和j,使得 nums[i]= nums[j],并且i和j的差的绝对值至多为 k。
示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
'''

class Solution:
    def containsNearbyDuplicate(self,nums):
        dct={}
        for i in range(len(nums)):
            if nums[i] in dct and dct[nums[i]]>=i-k:
                return True
            dct[nums[i]]=i
            
        return False
        
    
    
#220. 存在重复元素 III
'''
在整数数组 nums中，是否存在两个下标 i和j，使得 nums[i]和nums[j]的差的绝对值小于等于t,且满足i和j的差的绝对值也小于等于ķ。
如果存在则返回 true，不存在返回 false。
示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

'''

'''
首先，定义桶的大小是t+1, nums[i]//(t+1)决定放入几号桶,这样在一个桶里面的任意两个的绝对值差值都<=t
例如t=3, nums=[0 ,5, 1, 9, 3,4],那么0号桶就有[0,1,3],1号桶就有[4,5],2号桶就有[9]

先不考虑索引差值最大为K的限制，那么遍历nums每一个元素，并把他们放入相应的桶中，有两种情况会返回True

要放入的桶中已经有其他元素了，这时将nums[i]放进去满足差值<=t
可能存在前面一个桶的元素并且与nums[i]的差值<=t 或者 存在后面一个桶的元素并且与nums[i]的差值<=t

根据返回True的第一个条件，可以知道前后桶的元素最多也只能有一个。

接着考虑限制桶中的索引差最大为K,当i>=k的时候：
我们就要去删除存放着nums[i-k]的那个桶(编号为nums[i-k]//(t+1))
这样就能保证遍历到第i+1个元素时，全部桶中元素的索引最小值是i-k+1，就满足题目对索引的限制了

'''

class Solution:
    def containsNearbyAlmostDuplicate(self,nums):
        if t<0 or k<0:
            return False
        
        all_buckets={}
        bucket_size=t+1  #桶的大小设置成t+1更加方便
        
        for i in range(len(nums)):
            bucket_num=nums[i]//bucket_size   #放入哪个桶
            
            if bucket_num in all_buckets:   #桶中已经有元素了
                return True
            
            all_buckets[bucket_num]=nums[i]  #把nums[i]放入桶中
            
            if (bucket_num-1) in all_buckets and abs(all_buckets[bucket_num-1]-nums[i])<=t:  #检查前一个桶
                return True
            
            if (bucket_num+1) in all_buckets and abs(all_buckets[bucket_num+1]-nums[i])<=t:  #检查后一个桶
                return True
            
            #如果不构成返回条件，那么当i>=k时就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过K
            
            if i>=k:
                all_buckets.pop(nums[i-k]//bucket_size)
                
        return False
            
        






