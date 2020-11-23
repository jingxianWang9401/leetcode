# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:36:58 2020

@author: wangjingxian
"""

#剑指 Offer 48. 最长不含重复字符的子字符串

'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''



'''
方法一：动态规划 + 哈希表

动态规划解析：

状态定义：设动态规划列表dp，dp[j]代表以字符 s[j]为结尾的 “最长不重复子字符串” 的长度。

转移方程： 固定右边界 j，设字符 s[j]左边距离最近的相同字符为  s[i]，即 s[i]=s[j]。

当 i<0，即 s[j]左边无相同字符，则 dp[j]=dp[j−1]+1；
当 dp[j−1]<j−i，说明字符 s[i]在子字符串 dp[j−1]区间之外 ，则 dp[j]=dp[j−1]+1；
当 dp[j−1]≥j−i，说明字符 s[i]在子字符串 dp[j−1]区间之中 ，则 dp[j]的左边界由 s[i]决定，即 dp[j]=j−i；


当 i<0时，由于 dp[j−1]≤j恒成立，因而 dp[j−1]<j−i恒成立，因此分支 1. 和 2. 可被合并。

dp[j]={dp[j−1]+1, dp[j-1] < j - i \\
j-i ,dp[j−1]≥j−i​
返回值： max⁡(dp) ，即全局的 “最长不重复子字符串” 的长度。

哈希表统计： 遍历字符串 sss 时，使用哈希表（记为 dicdicdic ）统计 各字符最后一次出现的索引位置 。
左边界 iii 获取方式： 遍历到 s[j]s[j]s[j] 时，可通过访问哈希表 dic[s[j]]dic[s[j]]dic[s[j]] 获取最近的相同字符的索引 iii 。

复杂度分析：
时间复杂度 O(N)： 其中N为字符串长度，动态规划需遍历计算dp列表。
空间复杂度 O(1)： 字符的 ASCII 码范围为 000 ~ 127，哈希表 dic最多使用 O(128)=O(1)大小的额外空间。

'''

class Solution:
    def lengthOfLongestSubstring(self,s):
        dic={}
        res=tmp=0
        for j in range(len(s)):
            i=dic.get(s[j],-1)#获取索引i
            dic[s[j]]=j #更新哈希表
            tmp=tmp+1 if tmp<j-i else j-i #dp[j - 1] -> dp[j]
            res=max(res,tmp)
        return res
    
    
    





'''
方法三：双指针 + 哈希表

本质上与方法一类似，不同点在于左边界 iii 的定义。


哈希表 dicdicdic 统计： 指针 jjj 遍历字符 sss ，哈希表统计字符 s[j]s[j]s[j] 最后一次出现的索引 。
更新左指针 iii ： 根据上轮左指针 iii 和 dic[s[j]]dic[s[j]]dic[s[j]] ，每轮更新左边界 iii ，保证区间 [i+1,j][i + 1, j][i+1,j] 内无重复字符且最大。

i=max⁡(dic[s[j]],i)i = \max(dic[s[j]], i)
i=max(dic[s[j]],i)

更新结果 resresres ： 取上轮 resresres 和本轮双指针区间 [i+1,j][i + 1,j][i+1,j] 的宽度（即 j−ij - ij−i ）中的最大值。

res=max⁡(res,j−i)res = \max(res, j - i)
res=max(res,j−i)
 复杂度分析：

时间复杂度 O(N)： 其中 N为字符串长度，动态规划需遍历计算 dp列表。
空间复杂度 O(1)： 字符的 ASCII 码范围为 0~ 127，哈希表 dic最多使用 O(128)=O(1)大小的额外空间。

'''

class Solution:
    def lengthOfLongestSubstring(self,s):
        dic,res,i={},0,-1
        for j in range(len(s)):
            if s[j] in dic:
                i=max(dic[s[j]],i)
            dic[s[j]]=j#哈希表记录
            res=max(res,j-i)
        return res















            
            














