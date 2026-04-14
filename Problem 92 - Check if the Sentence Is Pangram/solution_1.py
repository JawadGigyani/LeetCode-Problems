class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = [0] * 26
        sentence = list(sentence)
        for alph in sentence:
            freq[ord(alph) - 97] += 1

        return False if 0 in freq else True