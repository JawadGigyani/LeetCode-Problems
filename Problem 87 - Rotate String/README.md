# 796. Rotate String

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/rotate-string/description/)

---

## Problem Description

Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of **shifts** on `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

---

## Examples

**Example 1:**

```
Input: s = "abcde", goal = "cdeab"  
Output: true  
```

**Example 2:**

```
Input: s = "abcde", goal = "abced"  
Output: false  
```

---

## Constraints

- `1 <= s.length, goal.length <= 100`  
- `s` and `goal` consist of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used the **string concatenation (double string) trick**:

1. **Length check**: If `s` and `goal` have different lengths, return `False` immediately, as rotation doesn't change length.
2. **Concatenate**: Create a new string `s + s`.
3. **Substring check**: Return whether `goal` is a substring of `s + s`.

### Why This Approach?

If `goal` is a valid rotation of `s`, then `goal` must be a contiguous substring within `s + s`:
- **Time Complexity:** O(n) — Checking if `goal` is a substring of `s + s` takes linear time in Python using the `in` operator.
- **Space Complexity:** O(n) — For creating the concatenated string `s + s`.

The intuition is that concatenating a string with itself (`s + s`) produces a sequence that contains every possible rotation of `s`. For example, if `s = "abcde"`, then `s + s = "abcdeabcde"`. Every substring of length 5 within this new string is a valid rotation of `s`. If `goal` is found within it, and lengths match, it must be a valid rotation.

---
