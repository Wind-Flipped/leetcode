# -*- coding: utf-8 -*-
# @Time : 2025/10/21 20:37
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树展开为链表#114.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        curr = root
        while curr:
            if curr.left:
                left_node = curr.left
                predecessor = left_node
                # 找到左子树的最右节点
                while predecessor.right:
                    predecessor = predecessor.right
                right_node = curr.right
                predecessor.right = right_node
                curr.left = None
                curr.right = left_node
            curr = curr.right