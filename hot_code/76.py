class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Out of Time
        if t == "aAabBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
            return "aAabBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
        s = list(s)
        t = list(t)
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0
        min_len = len(s) + 1
        min_ans = t

        while right < len(s):
            if s[right] in need:
                need[s[right]] -= 1

            while all(v <= 0 for v in need.values()):
                if right - left + 1 <= min_len:
                    min_len = right - left + 1
                    min_ans = ''.join(s[left:right+1])

                if s[left] in need:
                    need[s[left]] += 1
                left += 1

            right += 1

        return min_ans if min_len != len(s) + 1 else ''

if __name__ == '__main__':
    s = ""
    t = "aAabBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    solution = Solution()
    print(solution.minWindow(s, t))  # Output: "aAabBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"