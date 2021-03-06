from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        res = 0
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1] + 1
                    res = max(res, memo[i][j])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
    print(result)
