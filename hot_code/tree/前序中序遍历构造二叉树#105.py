# -*- coding: utf-8 -*-
# @Time : 2025/10/21 20:52
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 前序中序遍历构造二叉树#105.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val2index = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            in_root_index = val2index[root_val]
            left_subtree_size = in_root_index - in_left

            root.left = build(pre_left + 1, pre_left + left_subtree_size, in_left, in_root_index - 1)
            root.right = build(pre_left + left_subtree_size + 1, pre_right, in_root_index + 1, in_right)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)