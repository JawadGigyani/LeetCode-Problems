class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        count = 0
        nums.sort()
        while low < high:
            if (nums[low] + nums[high]) == k:
                count += 1
                low += 1 
                high -= 1
            elif (nums[low] + nums[high]) < k:
                low += 1
            else:
                high -= 1
        return count