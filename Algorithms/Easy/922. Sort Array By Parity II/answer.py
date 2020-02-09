from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 != 0:
                while A[j] % 2 != 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


if __name__ == "__main__":
    s = Solution()
    result = s.sortArrayByParityII([4, 2, 5, 7])
    print(result)
