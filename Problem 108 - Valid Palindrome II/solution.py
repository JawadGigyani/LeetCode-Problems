class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        count = 0
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if count == 1:
                    return False
                
                l, r = left, right - 1
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    return True
                
                l, r = left + 1, right
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                return l >= r
        
        return True