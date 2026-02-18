class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(st):
            stack = []
            for ch in st:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)

        return build(s) == build(t)