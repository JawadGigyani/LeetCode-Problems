# 459. Repeated Substring Pattern

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/repeated-substring-pattern/description/)

---

## Problem Description

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

---

## Examples

**Example 1:**

```
Input: s = "abab"  
Output: true  
Explanation: It is the substring "ab" twice.
```

**Example 2:**

```
Input: s = "aba"  
Output: false  
```

**Example 3:**

```
Input: s = "abcabcabcabc"  
Output: true  
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
```

---

## Constraints

- `1 <= s.length <= 10⁴`  
- `s` consists of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used the **double string trick**:

1. **Concatenate** `s` with itself to form `s + s`
2. **Remove** the first and last characters: `(s + s)[1:-1]`
3. **Check** if `s` exists within this modified string
4. **Return** the result.

### Why This Approach?

If `s` is made of a repeating pattern, then `s + s` contains overlapping copies that reconstruct `s` even after trimming the edges:
- **Time Complexity:** O(n) — String concatenation and substring search
- **Space Complexity:** O(n) — The doubled string

The intuition: if `s = "abab"`, then `s + s = "abababab"`. After trimming: `"bababa"`. The original `"abab"` still appears inside because the repeating pattern creates natural overlaps. If `s` is *not* a repeated pattern (e.g., `"aba"`), trimming the ends destroys the only occurrence of `s`, so the check fails. An elegant one-liner solution.

---
