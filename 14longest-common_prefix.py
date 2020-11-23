# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:53:13 2020

@author: wangjingxian
"""

#14. 最长公共前缀
'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。


'''
#方法一：利用python内置的zip()和set()函数
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
    
'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
利用 * 号操作符，可以将元组解压为列表。
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]

set() 函数创建一个无序不重复元素的集合，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等，返回新的集合对象
a_list=['a','b','c','d','a','b']
one=set(a_list)
print(one)                      
#set(['a', 'c', 'b', 'd'])

'''




#方法二：横向扫描
'''
用 LCP(S1…Sn)\textit{LCP}(S_1 \ldots S_n)LCP(S1​…Sn​) 表示字符串 S1…SnS_1 \ldots S_nS1​…Sn​ 的最长公共前缀。
可以得到以下结论：
LCP(S1…Sn)=LCP(LCP(LCP(S1,S2),S3),…Sn)\textit{LCP}(S_1 \ldots S_n) = \textit{LCP}(\textit{LCP}(\textit{LCP}(S_1, S_2),S_3),\ldots S_n)
LCP(S1​…Sn​)=LCP(LCP(LCP(S1​,S2​),S3​),…Sn​)
基于该结论，可以得到一种查找字符串数组中的最长公共前缀的简单方法。依次遍历字符串数组中的每个字符串，
对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。

如果在尚未遍历完所有的字符串时，最长公共前缀已经是空串，则最长公共前缀一定是空串，
因此不需要继续遍历剩下的字符串，直接返回空串即可。
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

#时间复杂度：O(mn)O(mn)O(mn)，其中 mmm 是字符串数组中的字符串的平均长度，nnn 是字符串的数量。
#最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。



#方法三：纵向扫描
'''
纵向扫描时，从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，
如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != c: 
                       return strs[0][:i]        
        return strs[0]

'''
时间复杂度：O(mn)，其中m是字符串数组中的字符串的平均长度，n是字符串的数量。
最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。
'''

