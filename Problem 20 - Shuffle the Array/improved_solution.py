class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for i in range(n) for num in (nums[i], nums[i+n])]