class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        if not (a + b > c and b + c > a and c + a > b):
            return "none"

        if a == b == c:
            return "equilateral"

        elif a == b or b == c or c == a:
            return "isosceles"

        else:
            return "scalene"