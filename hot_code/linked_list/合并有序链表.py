# -*- coding: utf-8 -*-
# @Time : 2025/10/17 18:40
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 合并有序链表.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        ans = None
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                if head:
                    head.next = p1
                    head = head.next
                    p1 = p1.next
                else:
                    head = p1
                    p1 = p1.next
                    ans = list1 # 记录答案的头节点
            else:
                if head:
                    head.next = p2
                    head = head.next
                    p2 = p2.next
                else:
                    head = p2
                    p2 = p2.next
                    ans = list2
        if p1:
            head.next = p1
        if p2:
            head.next = p2
        return ans