# 921. Minimum Add to Make Parentheses Valid

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)

---

## Problem Description

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(()))"` or a closing parenthesis to be `"())))"`.

Return the **minimum number of moves** required to make `s` valid.

---

## Examples

**Example 1:**

```text
Input: s = "())"
Output: 1
```

**Example 2:**

```text
Input: s = "((("
Output: 3
```

---

## Constraints

- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`.

---

## Solution Strategy

To solve this problem, I used a **Stack** along with a counter to track unmatched parentheses:

1. Initialise an empty list `stack` to keep track of unmatched opening parentheses `'('`.
2. Initialise a `count` variable to keep track of unmatched closing parentheses `')'`.
3. Iterate through each character `ch` in the string `s`:
   - If `ch` is an opening parenthesis `'('`, push it onto the `stack`.
   - If `ch` is a closing parenthesis `')'`, check the stack:
     - If the stack is not empty (which means there is a matching `'('` available), pop from the stack to pair them up.
     - If the stack is empty, it means we have a closing parenthesis without a matching opening parenthesis before it. Increment `count`.
4. After processing the entire string, the stack will contain all the unmatched opening parentheses, and `count` will represent all unmatched closing parentheses.
5. The minimum number of moves is the sum of `count` and the number of elements left in the `stack` (`len(stack)`).

### Why This Works

- The stack perfectly matches up valid pairs as we iterate from left to right.
- Any time we encounter a `')'` but have an empty stack, we *must* add an opening parenthesis to fix it, hence `count += 1`.
- Any `'('` left in the stack at the end of the loop means we reached the end of the string without finding matching closing parentheses. We *must* add closing parentheses to fix them, requiring exactly `len(stack)` moves.

## Complexity Analysis

- **Time Complexity:** `O(n)` where `n = len(s)`. We iterate through the string exactly once. Push and pop operations on a stack take `O(1)` time.
- **Space Complexity:** `O(n)` in the worst case (e.g., `s = "((("`), as all the opening parentheses are stored in the stack. *Note: This can be optimized to O(1) by replacing the stack with an integer that counts the number of unmatched opening parentheses.*
