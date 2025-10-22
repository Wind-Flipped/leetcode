# -*- coding: utf-8 -*-
# @Time : 2025/10/22 19:11
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 课程表#207.py
# @Project : leetcode

from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_courses = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                course = queue.popleft()
                visited_courses += 1
                for neighbor in graph[course]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        return visited_courses == numCourses