# -*- coding: utf-8 -*-
# @Time : 2025/10/23 20:45
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 完全平方数#279.py
# @Project : leetcode

from typing import List, Optional
class Solution:
    def numSquares(self, n: int) -> int:
        # 用 dp[i] 表示数字 i 能表示为完全平方数的最少数量
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]