class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l] == 0:
                del nums[l]
                nums.append(0)
                r -= 1
            if nums[l] != 0:
                l += 1