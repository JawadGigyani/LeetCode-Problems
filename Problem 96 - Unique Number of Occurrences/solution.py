from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        checked = set()

        for val in freq:
            if freq[val] in checked:
                return False
            checked.add(freq[val]) 
        
        return True