from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] >= 1 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    solution = Solution()
    ans = solution.firstMissingPositive(nums)
    print(ans)