# -*- coding: utf-8 -*-
# @Time : 2025/10/17 18:50
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 两数相加#2.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        ans = None
        # 可以直接 while l1 or l2，然后在循环内判断 l1 和 l2 是否为空
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            sum = sum % 10
            if head is None:
                head = ListNode(sum)
                ans = head
            else:
                new_node = ListNode(sum)
                head.next = new_node
                head = head.next

            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            carry = sum // 10
            sum = sum % 10
            if head is None:
                head = ListNode(sum)
                ans = head
            else:
                new_node = ListNode(sum)
                head.next = new_node
                head = head.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            carry = sum // 10
            sum = sum % 10
            if head is None:
                head = ListNode(sum)
                ans = head
            else:
                new_node = ListNode(sum)
                head.next = new_node
                head = head.next
            l2 = l2.next
        if carry: # 最后还有进位
            new_node = ListNode(carry)
            head.next = new_node
        return ans