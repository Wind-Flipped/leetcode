# -*- coding: utf-8 -*-
# @Time : 2025/10/22 16:01
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树的最大路径和#124.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = - 100000
        def max_gain(node):
            if not node:
                return 0
            left_max = max(max_gain(node.left), 0)
            right_max = max(max_gain(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)
        max_gain(root)
        return self.max_sum