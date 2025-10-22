# -*- coding: utf-8 -*-
# @Time : 2025/10/22 18:17
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 岛屿数量#200.py
# @Project : leetcode

from typing import List, Optional


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0' or visited[r][c]:
                return
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1
        return island_count