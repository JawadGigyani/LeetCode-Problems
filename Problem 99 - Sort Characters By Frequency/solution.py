class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        s_list = []
 
        for char, count in sorted_freq:
            s_list.append(char * count)
        
        return ''.join(s_list)