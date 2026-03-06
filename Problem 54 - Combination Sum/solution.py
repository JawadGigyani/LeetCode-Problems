class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, current, remaining):
            if remaining == 0:
                result.append(current.copy())
                return
            if remaining < 0:
                return
            for i in range(index, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return result