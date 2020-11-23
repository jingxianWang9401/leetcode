# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:47:09 2020

@author: wangjingxian
"""

#7. 整数反转
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

'''

#简单思路

class Solution:
    def reverse_force(self,x):
        if -10<x<10:
            return x
        str_x=str(x)
        if str_x[0]!="-":
            str_x=str_x[::-1]
            x=int(str_x)
        else:
            str_x=str_x[:0:-1]
            x=int(str_x)
            x=-x
        return x if -2147483648<x<2147483647 else 0
    
    
    










