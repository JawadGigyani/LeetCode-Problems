class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        output_word = []
        
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                output_word.append(word1[i])
                i += 1
            if j < len(word2):
                output_word.append(word2[j])
                j += 1
        
        return ''.join(output_word)