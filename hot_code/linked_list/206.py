# -*- coding: utf-8 -*-
# @Time : 2025/10/16 19:49
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 206.py
# @Project : leetcode

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代方法
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归方法
        if not head or not head.next:
            return head

        prev = self.reverseList2(head.next)
        head.next.next = head
        head.next = None # 防止链表成环，这一步容易想不到

        return prev