# 1754. Largest Merge Of Two Strings

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/largest-merge-of-two-strings/description/)

---

## Problem Description

You are given two strings `word1` and `word2`.  Construct a string `merge` by repeatedly performing one of the following operations while either string is non‑empty:

1. If `word1` is non‑empty, **append** its first character to `merge` and delete that character from `word1`.
2. If `word2` is non‑empty, **append** its first character to `merge` and delete that character from `word2`.

Return the **lexicographically largest** possible `merge`.

A string `a` is lexicographically larger than a string `b` (of the same length) if at the first position where they differ, `a` has a strictly larger character.

---

## Examples

**Example 1:**

```text
Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"
Explanation:
One optimal sequence of choices is:
- take from `word1` → merge = "c",   word1 = "abaa", word2 = "bcaaa"
- take from `word2` → merge = "cb",  word1 = "abaa", word2 = "caaa"
- take from `word2` → merge = "cbc", word1 = "abaa", word2 = "aaa"
- take from `word1` → merge = "cbca", word1 = "baa",  word2 = "aaa"
- take from `word1` → merge = "cbcab", word1 = "aa",   word2 = "aaa"
- append the remaining five `a`s from both strings.
```

**Example 2:**

```text
Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"
```

---

## Constraints

- `1 <= word1.length, word2.length <= 3000`
- `word1` and `word2` consist only of lowercase English letters.

---

## Solution Strategy

The key observation is that at each step we only need to compare the **remaining suffixes** of the two strings.  Whichever suffix is lexicographically larger will produce a larger final merge if we take its first character now.

1. Initialise two pointers `i` and `j` at the start of `word1` and `word2`.
2. While both pointers are within their strings:
   - Compare the remaining substrings `word1[i:]` and `word2[j:]`.
   - If `word1[i:]` is greater, append `word1[i]` to `merge` and increment `i`.
   - Otherwise, append `word2[j]` and increment `j`.
3. Once one string is exhausted, append the rest of the other string.
4. Join the collected characters into the final string.

The implementation mirrors the reference solution: a simple loop with a direct lexicographic comparison of the suffixes, followed by concatenation of the leftover parts.

---

## Why This Approach?

- **Correctness:** By always choosing the larger remaining suffix we guarantee that the current character is the best possible prefix for a maximal lexicographic result. Any alternative choice would start the merge with a smaller character at the first point of divergence, making the final string strictly smaller.
- **Simplicity:** The algorithm needs only two indices and a list to accumulate characters – no recursion, no extra data structures.
- **Efficiency:** Direct slicing (`word1[i:]`) is O(1) in Python because it creates a view of the underlying string; the actual comparison scans the characters only as needed.

### Complexity
- **Time Complexity:** O(n + m) where `n = len(word1)` and `m = len(word2)`. Each character is examined at most once, and each suffix comparison also traverses at most the remaining characters, giving a linear overall bound.
- **Space Complexity:** O(n + m) for the output string (the `merge` list), plus O(1) auxiliary space.

---
