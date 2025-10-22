# -*- coding: utf-8 -*-
# @Time : 2025/10/22 15:30
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 路径总和3#437.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_count = {0: 1}
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            res = prefix_sum_count.get(current_sum - targetSum, 0)
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            res += dfs(node.left, current_sum)
            res += dfs(node.right, current_sum)
            prefix_sum_count[current_sum] -= 1
            return res
        return dfs(root, 0)