# -*- coding: utf-8 -*-
# @Time : 2025/10/21 16:50
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 验证二叉搜索树.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low=-2**31 - 1, high=2**31 + 2):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            if not validate(node.right, val, high):
                return False
            if not validate(node.left, low, val):
                return False
            return True
        return validate(root)