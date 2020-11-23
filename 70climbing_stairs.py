# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:59:42 2020

@author: wangjingxian
"""

#70. 爬楼梯

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''


# 直接递归解法，容易超时，python可以加个缓存装饰器，这样也算是将递归转换成迭代的形式了
# 除了这种方式，还有增加步长来递归，变相的减少了重复计算
# 还有一种方法，在递归的同时，用数组记忆之前得到的结果，也是减少重复计算

class Solution:
    @functools.lru_cache(100)#缓存装饰器
    def climbStairs(self,n):
        if n==1:return 1
        if n==2:return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
    
# 直接DP，时间复杂度O（n),新建一个字典或者数组来存储以前的变量，空间复杂度O(n),推荐
class Solution:
    def climbStairs(self,n):
        dp={}
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
#
    
    
    
    
    
    