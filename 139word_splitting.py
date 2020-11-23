# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:18:10 2020

@author: wangjingxian
"""

#139. 单词拆分
'''
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
	拆分时可以重复使用字典中的单词。
	你可以假设字典中没有重复的单词。


示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。


示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。


示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

'''


'''
动态规划
1、初始化 dp=[False,⋯ ,False]，长度为 n+1。n为字符串长度。dp[i]表示s的前i位是否可以用 wordDict中的单词表示。

2、初始化 dp[0]=True，空字符可以被表示。

3、遍历字符串的所有子串，遍历开始索引 i，遍历区间 [0,n)：
      遍历结束索引j，遍历区间 [i+1,n+1)： 
            若 dp[i]=True且 s[i,⋯ ,j)在 wordlist中：dp[j]=True。
            解释：dp[i]=True说明 s的前 i位可以用 wordDict表示，则 s[i,⋯ ,j)出现在 wordDict中，说明s的前j位可以表示。
4、返回 dp[n]

时间复杂度：O(n2)
空间复杂度：O(n)
'''


class Solution:
    def wordBreak(self,s,wordDict):
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
                    
        return dp[-1]















