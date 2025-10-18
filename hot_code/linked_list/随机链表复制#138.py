#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/10/18 17:11
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 随机链表复制#138.py
# @Software: PyCharm

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p1 = head
        if not p1:
            return None
        while p1:
            # 先复制一遍节点，插入到原节点后面
            new_node = Node(p1.val)
            p2 = p1.next
            p1.next = new_node
            new_node.next = p2
            p1 = p2
        p1 = head
        while p1:
            # 复制random指针
            if p1.random:
                p1.next.random = p1.random.next
            p1 = p1.next.next
        ans = head.next
        p1 = head
        while p1 and p1.next.next:
            p2 = p1.next.next
            p1.next.next = p1.next.next.next
            p1 = p2

        return ans

if __name__ == '__main__':
    solution = Solution()
    # Test cases can be added here to test the functionality
