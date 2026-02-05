class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1

        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return m
                break
            elif target > nums[m]:
                l = m+1
            elif target < nums[m]:
                h = m-1
        return -1