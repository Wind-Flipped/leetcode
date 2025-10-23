# -*- coding: utf-8 -*-
# @Time : 2025/10/23 21:09
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 最长递增子序列#300.py
# @Project : leetcode

from typing import List, Optional

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp [i] 表示以 nums[i] 结尾的最长递增子序列的长度
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)