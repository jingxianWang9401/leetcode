# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:13:39 2020

@author: wangjingxian
"""

#200. 岛屿数量

'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1


示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
'''



'''
思路一：深度优先遍历DFS
目标是找到矩阵中 “岛屿的数量” ，上下左右相连的 1 都被认为是连续岛屿。
dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。

从 (i, j) 向此点的上下左右 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 做深度搜索。
终止条件：
(i, j) 越过矩阵边界;
grid[i][j] == 0，代表此分支已越过岛屿边界。

搜索岛屿的同时，执行 grid[i][j] = '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。
目标是找到矩阵中 “岛屿的数量” ，上下左右相连的 1 都被认为是连续岛屿。
dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。

从 (i, j) 向此点的上下左右 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 做深度搜索。

终止条件：
     (i, j) 越过矩阵边界;
     grid[i][j] == 0，代表此分支已越过岛屿边界。

搜索岛屿的同时，执行 grid[i][j] = '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。

主循环：
遍历整个矩阵，当遇到 grid[i][j] == '1' 时，从此点开始做深度优先搜索 dfs，岛屿数 count + 1 且在深度优先搜索中删除此岛屿。
最终返回岛屿数 count 即可。

复杂度分析:
时间复杂度：O(MN)，其中 M 和 N分别为行数和列数。
空间复杂度：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 MN。
'''

class Solution:
    def numIslands(self,grid:[[str]]) ->int:
        def dfs(grid,i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j]=='0':return 
            grid[i][j]='0'
            dfs(grid,i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)
            
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(grid,i,j)
                    count+=1
                    
        return count
    
    
    
    
'''
方法二：广度优先遍历 BFS
主循环和思路一类似，不同点是在于搜索某岛屿边界的方法不同。
bfs 方法：
借用一个队列 queue，判断队列首部节点 (i, j) 是否未越界且为 1：

若是则置零（删除岛屿节点），并将此节点上下左右节点 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 加入队列；
若不是则跳过此节点；

循环 pop 队列首节点，直到整个队列为空，此时已经遍历完此岛屿。
复杂度分析


时间复杂度：O(MN)，其中 M和 N分别为行数和列数。

空间复杂度：O(min⁡(M,N)，在最坏情况下，整个网格均为陆地，队列的大小可以达到 min⁡(M,N)。

'''

class Solution:
    def numIslands(self,grid:[[str]]) ->int:
        def bfs(grid,i,j):
            queue=[[i,j]]
            while queue:
                [i,j]=queue.pop(0)
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
                    grid[i][j]='0'
                    queue+=[[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
                    
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='0':continue
                bfs(grid,i,j)
                count+=1
                
        return count
    
                    






