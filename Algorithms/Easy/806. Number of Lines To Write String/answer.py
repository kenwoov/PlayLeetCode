from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c)-ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w
        return [lines, width]


if __name__ == "__main__":
    s = Solution()
    result = s.numberOfLines([4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                              10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "bbbcccdddaaa")
    print(result)
