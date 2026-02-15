class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        count = 0
        max_ones = 0

        for right in range(n):
            if nums[right] == 0:
                count += 1
            
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            
            max_ones = max(max_ones, right - left + 1)
        return max_ones