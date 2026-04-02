class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        count = 0
        for jewel in jewels:
            if jewel in freq:
                count += freq[jewel]
        
        return count