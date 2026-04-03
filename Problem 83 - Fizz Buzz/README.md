# 412. Fizz Buzz

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/fizz-buzz/description/)

---

## Problem Description

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by `3` and `5`.
- `answer[i] == "Fizz"` if `i` is divisible by `3`.
- `answer[i] == "Buzz"` if `i` is divisible by `5`.
- `answer[i] == i` (as a string) if none of the above conditions are true.

---

## Examples

**Example 1:**

```
Input: n = 3  
Output: ["1","2","Fizz"]  
```

**Example 2:**

```
Input: n = 5  
Output: ["1","2","Fizz","4","Buzz"]  
```

**Example 3:**

```
Input: n = 15  
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]  
```

---

## Constraints

- `1 <= n <= 10⁴`

---

## Solution Strategy

To solve this problem, I used a **conditional chaining** approach:

1. **Initialize** an empty list `res`
2. **Iterate** from `1` to `n` (inclusive):
   - If `i` is divisible by both `3` and `5`, append `'FizzBuzz'`
   - Else if `i` is divisible by `3`, append `'Fizz'`
   - Else if `i` is divisible by `5`, append `'Buzz'`
   - Otherwise, append `str(i)`
3. **Return** `res`.

### Why This Approach?

The order of conditions matters — checking divisibility by both `3` and `5` first prevents it from being caught by the individual `3` or `5` checks:
- **Time Complexity:** O(n) — One pass from `1` to `n`
- **Space Complexity:** O(n) — The result list stores `n` strings

A straightforward and classic implementation. The `if/elif/else` chain ensures exactly one label is assigned per number, with the most specific condition (`% 15`) evaluated first.

---
