# -*- coding: utf-8 -*-
# @Time : 2025/10/27 20:51
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 最长回文子串#5.py
# @Project : leetcode

from typing import List, Optional


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # dp[i][j] 表示 s[i:j+1] 是否是回文串
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_length = 1

        # 所有长度为 1 的子串都是回文串
        for i in range(n):
            dp[i][i] = True

        # 检查长度为 2 的子串
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # 检查长度大于 2 的子串
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]