# -*- coding: utf-8 -*-
# @Time : 2025/10/21 16:46
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 将有序数组转换为二叉搜索树#108.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def getBST(left, right):
            # 这是个闭区间
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(val=nums[mid])
            root.left = getBST(left, mid - 1)
            root.right = getBST(mid + 1, right)
            return root
        return getBST(0, len(nums) - 1)