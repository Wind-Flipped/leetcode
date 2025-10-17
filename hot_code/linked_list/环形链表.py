# -*- coding: utf-8 -*-
# @Time : 2025/10/16 20:23
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 环形链表.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not slow:
            return False
        fast = head.next
        if not fast:
            return False
        while slow != fast:
            if not fast or not fast.next: # 注意这里的判断条件，只判断快指针和快指针的下一个节点
                return False
            slow = slow.next
            fast = fast.next.next

        return slow != None
