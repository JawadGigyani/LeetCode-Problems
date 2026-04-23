class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <=2:
            return list(set(nums))
        
        freq = Counter(nums)

        sorted_freq = sorted(freq.items(), key = lambda x:x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(sorted_freq[i][0])

        return res