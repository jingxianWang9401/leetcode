# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:23:14 2020

@author: wangjingxian
"""
#208. 实现 Trie (前缀树)
'''
实现一个 Trie (前缀树,字典树，单词查找树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true

说明:
	你可以假设所有的输入都是由小写字母 a-z 构成的。
	保证所有输入均为非空字符串。

应用：
Trie (发音为 "try") 或前缀树是一种树数据结构，用于检索字符串数据集中的键。这一高效的数据结构有多种应用：
 1. 自动补全：谷歌、百度的搜索建议
 比如用户搜索输入goo,下面就会建议google\google search
 2. 拼写检查:检查单词是否拼写错误
 3、IP路由：最长前缀匹配
 4、九宫格打字预测
 5、单词游戏


操作一：向 Trie 树中插入键
我们通过搜索 Trie 树来插入一个键。我们从根开始搜索它对应于第一个键字符的链接。有两种情况：
链接存在。沿着链接移动到树的下一个子层。算法继续搜索下一个键字符。
链接不存在。创建一个新的节点，并将它与父节点的链接相连，该链接与当前的键字符相匹配。
重复以上步骤，直到到达键的最后一个字符，然后将当前节点标记为结束节点，算法完成。
时间复杂度：O(m)，其中 m为键长。


操作二：在 Trie 树中查找键
每个键在 trie 中表示为从根到内部节点或叶的路径。我们用第一个键字符从根开始，检查当前节点中与键字符对应的链接。
有两种情况：
存在链接。我们移动到该链接后面路径中的下一个节点，并继续搜索下一个键字符。
不存在链接。若已无键字符，且当前结点标记为 isEnd，则返回 true。否则有两种可能，均返回 false :
1）还有键字符剩余，但无法跟随 Trie 树的键路径，找不到键。
2）没有键字符剩余，但当前结点没有标记为 isEnd。也就是说，待查找键只是Trie树中另一个键的前缀。
时间复杂度 : O(m)算法的每一步均搜索下一个键字符。最坏的情况下需要 m次操作。


错做三：查找Trie树中的键前缀
该方法与在 Trie 树中搜索键时使用的方法非常相似。我们从根遍历 Trie 树，直到键前缀中没有字符，
或者无法用当前的键字符继续 Trie 中的路径。与上面提到的“搜索键”算法唯一的区别是，到达键前缀的末尾时，
总是返回 true。我们不需要考虑当前 Trie 节点是否用 “isend” 标记，因为我们搜索的是键的前缀，而不是整个键。
时间复杂度 : O(m)。

'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['word'] = word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.trie
        for c in word:
            if c not in root:
                return False
            root = root[c]
        return "word" in root


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

