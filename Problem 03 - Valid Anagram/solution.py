class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = list(s)
        ts = list(t)

        st.sort()
        ts.sort()

        if st == ts:
            return True
        else:
            return False