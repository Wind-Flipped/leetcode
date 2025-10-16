from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
    print(s.maxSlidingWindow([1], 1))  # Output: [1]
    print(s.maxSlidingWindow([1,-1], 1))  # Output: [1,-1]
    print(s.maxSlidingWindow([9,11], 2))  # Output: [11]
    print(s.maxSlidingWindow([4,-2], 2))  # Output: [4]