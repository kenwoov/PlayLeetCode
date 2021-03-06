from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        size = 1 << n
        for i in range(size):
            res.append((i >> 1) ^ i)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.grayCode(2)
    print(result)
