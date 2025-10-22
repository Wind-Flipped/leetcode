# -*- coding: utf-8 -*-
# @Time : 2025/10/22 18:48
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 腐烂的橘子#994.py
# @Project : leetcode

from typing import List, Optional


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        cols, rows = len(grid), len(grid[0])
        from collections import deque

        cur_rotten = deque()
        fresh_count = 0
        for c in range(cols):
            for r in range(rows):
                if grid[c][r] == 2:
                    cur_rotten.append((c, r))
                elif grid[c][r] == 1:
                    fresh_count += 1

        minutes = 0
        if not cur_rotten:
            return 0 if fresh_count == 0 else -1
        while cur_rotten:
            size = len(cur_rotten)
            for _ in range(size):
                x, y = cur_rotten.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < cols and 0 <= ny < rows and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        cur_rotten.append((nx, ny))

            minutes += 1
        return minutes - 1 if fresh_count == 0 else -1