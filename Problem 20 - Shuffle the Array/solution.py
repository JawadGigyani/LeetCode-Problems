class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 1

        while l < len(nums):
            nums.insert(l, nums[n])
            n += 1
            del nums[n]
            l += 2
        return  nums