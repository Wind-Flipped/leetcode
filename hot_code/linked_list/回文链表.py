# -*- coding: utf-8 -*-
# @Time : 2025/10/16 20:08
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 回文链表.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        ans = True
        p1 = head
        p2 = second_half_start
        while p1 and p2:
            if p1.val != p2.val:
                ans = False
                break
            p1 = p1.next
            p2 = p2.next
        return ans


    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None: # 注意这里的判断条件
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
