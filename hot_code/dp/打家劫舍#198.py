# -*- coding: utf-8 -*-
# @Time : 2025/10/23 20:31
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 打家劫舍#198.py
# @Project : leetcode

from typing import List, Optional


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]