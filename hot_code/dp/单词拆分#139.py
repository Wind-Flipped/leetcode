# -*- coding: utf-8 -*-
# @Time : 2025/10/23 21:06
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 单词拆分#139.py
# @Project : leetcode

from typing import List, Optional


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        # 用 dp[i] 表示字符串 s 的前 i 个字符能否被拆分成字典中的单词
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]