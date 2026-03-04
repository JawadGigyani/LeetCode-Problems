class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        max_length = 0

        while right < len(s):
            window =  s[left:right+1]
            if len(window) == len(set(window)):
                len_of_substr = right - left + 1
                max_length = max(max_length, len_of_substr)
                right += 1
            else:
                left += 1
        return max_length