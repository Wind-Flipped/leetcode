# -*- coding: utf-8 -*-
# @Time : 2025/10/20 19:59
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 二叉树的最近公共祖先#236.py
# @Project : leetcode

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root
        def contain_node(root, p, q):
            if not root:
                return False
            l_contain = contain_node(root.left, p, q)
            r_contain = contain_node(root.right, p, q)
            if (l_contain and r_contain) or ((root == p or root == q) and (l_contain or r_contain)):
                self.ans = root
                return True
            return l_contain or r_contain or root == p or root == q


        contain_node(root, p, q)
        return self.ans
