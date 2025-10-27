#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/10/27 10:24
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 乘积最大子数组#152.py
# @Software: PyCharm

from typing import List, Optional
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -float('inf')
        max_pre = 1
        min_pre = 1
        for num in nums:
            max_pre, min_pre = max(max_pre * num, min_pre * num, num),\
                               min(max_pre * num, min_pre * num, num)
            ans = max(max_pre, ans)
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [-4, -3, -2]
    print(solution.maxProduct(nums))  # Output: 12