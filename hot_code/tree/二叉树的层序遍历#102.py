# -*- coding: utf-8 -*-
# @Time : 2025/10/21 16:18
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树的层序遍历#102.py
# @Project : leetcode

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from queue import Queue


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            level = []
            for _ in range(size):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(level)
        return res