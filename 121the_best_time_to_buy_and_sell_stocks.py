# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:55:38 2020

@author: wangjingxian
"""

#121. 买卖股票的最佳时机
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。 

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''



'''
方法一：一次遍历

遍历一遍数组，计算每次到当天为止的最小股票价格和最大利润。

复杂度分析

时间复杂度：O(n)，遍历了一遍数组。
空间复杂度：O(1)，使用了有限的变量。

'''
class Solution:
    def maxProfit(self,prices):
        minprice=float('inf')
        maxprofit=0
        for price in prices:
            minprice=min(minprice,price)
            maxprofit=max(maxprofit,price-minprice)
        return maxprofit
    
    



'''
方法二：动态规划
动态规划一般分为一维、二维、多维（使用状态压缩），对应形式为 dp(i)、dp(i)(j)、二进制dp(i)(j)。
1. 动态规划做题步骤

明确 dp(i)应该表示什么（二维情况：dp(i)(j)）；
根据 dp(i)和 dp(i−1)的关系得出状态转移方程；
确定初始条件，如 dp(0)。

2. 本题思路
其实方法一的思路不是凭空想象的，而是由动态规划的思想演变而来。这里介绍一维动态规划思想。
dp[i]表示前 i天的最大利润，因为我们始终要使利润最大化，则：
dp[i]=max(dp[i−1],prices[i]−minprice)


复杂度分析
时间复杂度：
O(n)
空间复杂度：
O(n)
'''

class Solution:
    def maxProfit(self,prices):
        n=len(prices)
        if n==0:return 0  #边界条件
        dp=[0]*n
        minprice=prices[0]
        
        for i in range(1,n):
            minprice=min(minprice,prices[i])
            dp[i]=max(dp[i-1],prices[i]-minprice)
        return dp[-1]










