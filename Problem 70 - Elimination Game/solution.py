class Solution:
    def lastRemaining(self, n: int) -> int:
        def solve(head, step, length, is_left):
            if length == 1:
                return head

            if is_left:
                head += step

            else:
                if length % 2 == 1:
                    head += step
                
            return solve(head, step * 2, length // 2, not is_left)

        return solve(1, 1, n, True)