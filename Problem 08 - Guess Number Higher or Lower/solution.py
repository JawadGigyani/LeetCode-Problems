class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n

        while low <= high:
            mid = (low+high) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1
