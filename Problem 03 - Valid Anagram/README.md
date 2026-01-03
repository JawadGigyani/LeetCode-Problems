# 242. Valid Anagram

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/valid-anagram/description/)

---

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

## Examples

**Example 1:**

```
Input: s = "anagram", t = "nagaram"  
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"  
Output: false
```

---

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`  
- `s` and `t` consist of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **sorting** approach:

1. **Convert both strings to lists** so we can sort them.
2. **Sort both lists** alphabetically.
3. **Compare the sorted lists**:
   - If they are equal, the strings are anagrams → return `True`
   - Otherwise, they are not anagrams → return `False`

### Why This Approach?

Sorting both strings and comparing them is a straightforward way to check if they contain the same characters with the same frequencies:
- **Time Complexity:** O(n log n) - Dominated by the sorting operation, where n is the length of the strings
- **Space Complexity:** O(n) - We create list copies of both strings for sorting

This approach is simple and intuitive. An alternative approach using hash maps (character frequency counters) could achieve O(n) time complexity, but for most practical cases, the sorting approach is clean and efficient enough.

---
