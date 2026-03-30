class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for num in range(len(nums)):
            nums[num] *= nums[num]
        nums.sort()
        return nums