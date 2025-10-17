# -*- coding: utf-8 -*-
# @Time : 2025/10/17 19:01
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 删除倒数结点#19.py
# @Project : leetcode

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # 使用哑节点简化边界条件
        fast = head
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        # slow is the target node before remove
        slow.next = slow.next.next
        return dummy.next