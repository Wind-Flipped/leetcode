# -*- coding: utf-8 -*-
# @Time : 2025/10/20 19:05
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树的最大深度#104.py
# @Project : leetcode

from typing import List, Optional
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        if not root:
            return 0
        q.put(root)
        depth = 0
        while q.qsize() > 0:
            size = q.qsize()
            for _ in range(size):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            depth += 1
        return depth