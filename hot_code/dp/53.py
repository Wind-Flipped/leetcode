from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        max_sum = -1000000
        for num in nums:
            if dp > 0:
                dp += num
                max_sum = max(max_sum, dp)
            else:
                dp = num
                max_sum = max(max_sum, dp)
        return max_sum

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(s.maxSubArray([1]))  # Output: 1
    print(s.maxSubArray([5,4,-1,7,8]))  # Output: 23