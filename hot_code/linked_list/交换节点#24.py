# -*- coding: utf-8 -*-
# @Time : 2025/10/17 19:29
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 交换节点#24.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        while current and current.next:
            p1 = current
            p2 = current.next
            # 交换节点
            current = p2.next
            p2.next = p1
            prev.next = p2
            prev = p1

        if current:
            prev.next = current
        else:
            prev.next = None # 要注意最后需要指向 None

        return dummy.next
