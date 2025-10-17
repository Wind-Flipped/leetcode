# -*- coding: utf-8 -*-
# @Time : 2025/10/17 19:51
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : k个一组翻转链表#25.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            p1 = head
            for i in range(k - 1):
                p1 = p1.next
                if not p1:
                    # 剩下的不足k个，直接返回结果
                    return dummy.next
            tail = p1
            new_head, new_tail = self.reverse_list(head, tail)
            prev.next = new_head
            prev = new_tail
            head = new_tail.next

        return dummy.next



    def reverse_list(self, head: Optional[ListNode], tail: Optional[ListNode]):
        prev = tail.next
        p1 = head
        while prev != tail:
            p2 = p1.next
            p1.next = prev
            prev = p1
            p1 = p2
        return tail, head
