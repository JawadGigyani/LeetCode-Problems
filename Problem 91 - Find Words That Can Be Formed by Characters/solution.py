from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total_len = 0

        for word in words:
            word_count = Counter(word)

            for ch in word_count:
                if word_count[ch] > char_count[ch]:
                    break
            else:
                total_len += len(word)

        return total_len