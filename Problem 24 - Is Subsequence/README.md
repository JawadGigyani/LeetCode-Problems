# 392. Is Subsequence

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/is-subsequence/description/)

---

## Problem Description

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

---

## Examples

**Example 1:**

```
Input: s = "abc", t = "ahbgdc"  
Output: true
```

**Example 2:**

```
Input: s = "axc", t = "ahbgdc"  
Output: false
```

---

## Constraints

- `0 <= s.length <= 100`  
- `0 <= t.length <= 10^4`  
- `s` and `t` consist only of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach:

1. **Initialize two pointers**: `first = 0` (for string `s`) and `second = 0` (for string `t`)
2. **Loop while both pointers are within bounds**:
   - If `s[first] == t[second]`, we found a matching character → move `first` forward
   - Always move `second` forward (we scan through `t` regardless)
3. **Return** whether `first == len(s)` — if we matched all characters of `s`, it's a subsequence.

### Why This Approach?

The two-pointer technique efficiently checks subsequence order:
- **Time Complexity:** O(n) - Where n is the length of `t` (we scan through it once)
- **Space Complexity:** O(1) - Only using two pointer variables

By advancing the `first` pointer only when a match is found, we ensure the characters of `s` appear in the correct relative order within `t`. If all characters are matched, `first` reaches the end of `s`.

---
