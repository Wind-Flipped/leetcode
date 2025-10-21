# -*- coding: utf-8 -*-
# @Time : 2025/10/21 20:14
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树的右视图#199.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        from queue import Queue
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if i == 0:
                    res.append(node.val)
                if node.right:
                    q.put(node.right)
                if node.left:
                    q.put(node.left)
        return res