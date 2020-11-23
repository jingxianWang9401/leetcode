# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 08:28:21 2020

@author: wangjingxian
"""

#17.电话号码的字母组合
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''

'''
方法一：回溯
当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
定义函数 backtrack(combination, nextdigit)，当 nextdigit 非空时，对于 nextdigit[0] 中的每一个字母 letter，
执行回溯 backtrack(combination + letter,nextdigit[1:]，直至 nextdigit 为空。最后将 combination 加入到结果中。

'''

class Solution:
    def letterCombinations(self,digits):
        if not digits:
            return []
        
        phone={'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']
                }
        def backtrack(conbination,nextdigit):
            if len(nextdigit)==0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination+letter,nextdigit[1:])
                    
        res=[]
        backtrack('',digits)
        return res
    
    
    
'''
方法二：队列
我们也可以使用队列，先将输入的 digits 中第一个数字对应的每一个字母入队，
然后将出队的元素与第二个数字对应的每一个字母组合后入队...直到遍历到 digits 的结尾。最后队列中的元素就是所求结果。

'''

class Solution:
    def letterCombinations(self,digits):
        if not digits:
            return []
        phone=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue=['']
        for digit in digits:
            for _ in range(len(queue)):
                tmp=queue.pop(0)
                for letter in phone[ord(digit)-50]:
                    queue.append(tmp+letter)
        return queue