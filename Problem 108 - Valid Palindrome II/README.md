# 680. Valid Palindrome II

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/valid-palindrome-ii/description/)

---

## Problem Description

Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

---

## Examples

**Example 1:**

```
Input: s = "aba"
Output: true
```

**Example 2:**

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**

```
Input: s = "abc"
Output: false
```

---

## Constraints

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **Two-Pointer** approach:

1. **Initialize** two pointers, `left` at the beginning (`0`) and `right` at the end (`len(s) - 1`) of the string.
2. **Loop** while `left < right`:
   - If the characters match (`s[left] == s[right]`), we move both pointers inward (`left += 1`, `right -= 1`).
   - If they **do not match**, we have found a discrepancy. Since we are allowed to delete at most *one* character, we have two options to fix this:
     1. **Delete the right character**: Check if the substring from `left` to `right - 1` is a valid palindrome using a temporary pair of pointers (`l`, `r`).
     2. **Delete the left character**: If the first check fails, test if the substring from `left + 1` to `right` is a valid palindrome.
   - We simulate both options purely through pointer adjustments. If either check completes successfully (`l >= r`), the string can form a palindrome and we return `True` or evaluate the expression. Otherwise, return `False`.
3. If the main loop finishes without encountering any mismatches, return `True`.

### Why This Approach?

This two-pointer approach checks the conditions in-place, avoiding the overhead of creating new strings via slicing or relying on recursion.

- **Time Complexity:** O(n) — In the worst-case scenario, the outer loop and the inner sub-checks combined will process each character at most twice, resulting in a strictly linear runtime.
- **Space Complexity:** O(1) — We only use a few integer variables (`left`, `right`, `l`, `r`, `count`) to track positions, requiring constant extra memory regardless of the string's length.
