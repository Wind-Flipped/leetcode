#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/10/27 10:40
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 分割等和子集#416.py
# @Software: PyCharm

from typing import List, Optional


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        if total % 2 != 0 or length == 1:
            return False
        target = total // 2
        # dp[i] 表示是否存在子集和为 i
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                # 需要从大到小计算
                dp[j] = dp[j] or dp[j - num]
        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 5]
    print(solution.canPartition(nums))  # Output: False
