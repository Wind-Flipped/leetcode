# -*- coding: utf-8 -*-
# @Time : 2025/10/20 20:17
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树的直径#543.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0
        def get_depth(root):
            if not root:
                return 0
            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)
            depth = max(left_depth, right_depth) + 1
            path = left_depth + right_depth
            self.max_path = max(self.max_path, path)
            return depth

        get_depth(root)
        return self.max_path
