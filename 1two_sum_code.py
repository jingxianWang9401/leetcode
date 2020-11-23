# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:25:48 2020

@author: wangjingxian
"""
#两数之和
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

import time
nums=[3,3]
target=6

#暴力搜索，时间复杂度很高
def two_sum1(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                array_index=[i,j]
                return array_index
            else:
                continue

t1=time.process_time()            
array_index=two_sum1(nums,target)            
t1=time.process_time()-t1


t2=time.time()
array_index=two_sum1(nums,target)   
t2=time.time()-t2


t3=time.perf_counter()
array_index=two_sum1(nums,target)
t3=time.perf_counter()-t3

print(t1,'\n',t2,'\n',t3)
print(array_index)


     
#时间复杂度很低，遍历列表同时查字典
def two_sum3(nums,target):
    nums_dic={}
    for i,num in enumerate(nums):
        if target-num in nums_dic:
            return [nums_dic[target-num],i]
        nums_dic[num]=i
        
        
t1=time.process_time()            
array_index=two_sum3(nums,target)            
t1=time.process_time()-t1


t2=time.time()
array_index=two_sum3(nums,target)   
t2=time.time()-t2


t3=time.perf_counter()
array_index=two_sum3(nums,target)
t3=time.perf_counter()-t3

print(t1,'\n',t2,'\n',t3)
print(array_index)        

    
    
    