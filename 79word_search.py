# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:45:11 2020

@author: wangjingxian
"""

#79. 单词搜索

'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
	board 和 word 中只包含大写和小写英文字母。
	1 <= board.length <= 200
	1 <= board[i].length <= 200
	1 <= word.length <= 10^3

'''

from typing import List

class Solution:
    '''
        (x-1,y)
(x,y-1)  (x,y)  (x,y+1)
        (x+1,y)   
    '''

    directions=[(0,-1),(-1,0),(0,1),(1,0)]
    
    def exist(self,board,word):
        m=len(board)
        if m==0:
            return False
        n=len(board[0])
        
        marked=[[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                #对每个格子都从头开始搜索
                if self._search_word(board,word,0,i,j,marked,m,n):
                    return True
        return False
    
    
    def _search_word(self,board,word,index,start_x,start_y,marked,m,n):
        
        #先写递归终止条件
        if index ==len(word)-1:
            return board[start_x][start_y]==word[index]
        
        #中间匹配了，再继续搜索
        
        if board[start_x][start_y]==word[index]:
            #先占住这个位置，搜索不成功的话要释放掉
            marked[start_x][start_y]=True
            
            for direction in self.directions:
                new_x=start_x+direction[0]
                new_y=start_y+direction[1]
                #如果这次search_word成功的话，就返回
                if 0<=new_x<m and 0<=new_y<n and not marked[new_x][new_y] and self._search_word(board,word,index+1,new_x,new_y,marked,m,n):
                    return True
        
            marked[start_x][start_y]=False 
    
        return False
        
    
    
    