class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key = lambda x: x[0])
        
        curr = left

        for start, end in ranges:
            if start <= curr:
                curr = max(curr, end + 1)

            elif curr > right:
                return True

        return curr > right