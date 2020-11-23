# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:50:24 2020

@author: wangjingxian
"""

#88. 合并两个有序数组
'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
	初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
	你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

'''

'''
#方法一 : 合并后排序
直觉
最朴素的解法就是将两个数组合并之后再排序。该算法只需要一行()，时间复杂度较差，为O((n+m)log⁡(n+m))。
这是由于这种方法没有利用两个数组本身已经有序这一点。
复杂度分析

时间复杂度 : O((n+m)log⁡(n+m))
空间复杂度 : O(1)

'''

class Solution(object):
    def merge(self,nums1,m,nums2,n):
        '''
        nums1:List[int]
        m:int
        nums2:List[int]
        n:int
        
        '''
        nums1[:]=sorted(nums1[:m]+nums2)
        
        
        
'''
方法二 : 双指针 / 从前往后
一般而言，对于有序数组可以通过 双指针法 达到O(n+m)的时间复杂度。
最直接的算法实现是将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。
由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方，也就需要 O(m)的空间复杂度。

复杂度分析
时间复杂度 : O(n+m)
空间复杂度 : O(m)

'''        

class Solution(object):
    def merge(self,nums1,m,nums2,n):
        #复制nums1数组
        nums1_copy=nums1[:m]
        nums1[:]=[]
        #两个指针指向nums1_copy和nums2
        p1=0
        p2=0
        
        while p1<m and p2<n:
            if nums1_copy[p1]<nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1+=1
            else:
                nums1.append(nums2[p2])
                p2+=1
        
        if p1<m:
            nums1[p1+p2:]=nums1_copy[p1:]
            
        if p2<n:
            nums1[p1+p2:]=nums2[p2:]
        

'''
方法三 : 双指针 / 从后往前
方法二已经取得了最优的时间复杂度O(n+m)，但需要使用额外空间。
这是由于在从头改变nums1的值时，需要把nums1中的元素存放在其他位置。

如果我们从结尾开始改写 nums1 的值又会如何呢？这里没有信息，因此不需要额外空间。

这里的指针p用于追踪添加元素的位置。
复杂度分析
时间复杂度 : O(n+m)
空间复杂度 : O(1)。
'''

class Solution(object):
    def merge(self,nums1,m,nums2,n):
        #两个指针分别指向nums1和nums2
        p1=m-1
        p2=n-1
        #指针指向nums1的末尾
        p=m+n-1
        #两个数组元素的比较
        while p1>=0 and p2>=0:
            if nums1[p1]<nums2[p2]:
                nums1[p]=nums2[p2]
                p2-=1
            else:
                nums1[p]=nums1[p1]
                p1-=1
            p-=1
        #从nums2添加剩余的元素
        nums1[:p2+1]=nums2[:p2+1]
           





        
