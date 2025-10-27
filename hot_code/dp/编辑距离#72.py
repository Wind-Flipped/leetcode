# -*- coding: utf-8 -*-
# @Time : 2025/10/27 20:31
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : 编辑距离#72.py
# @Project : leetcode

from typing import List, Optional

# -*- coding: utf-8 -*-
# @Time : 2025/10/27 18:39
# @Author : liuyunqi
# @Email : liuyunqi@buaa.edu.cn
# @File : test.py
# @Project : llm_project

from typing import List, Optional

def edit_distance(s1, s2):
    length1 = len(s1)
    length2 = len(s2)
    dp = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]
    for i in range(length2 + 1):
        dp[0][i] = i
    for j in range(length1 + 1):
        dp[j][0] = j

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[length1][length2]

if __name__ == '__main__':
    s1 = "abccs"
    s2 = "abssss"
    print(edit_distance(s1, s2))