# 345. Reverse Vowels of a String

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)

---

## Problem Description

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

---

## Examples

**Example 1:**

```
Input: s = "IceCreAm"  
Output: "AceCreIm"  
Explanation: The vowels in s are ['I', 'e', 'e', 'A'].
On reversing the vowels, s becomes "AceCreIm".
```

**Example 2:**

```
Input: s = "leetcode"  
Output: "leotcede"  
```

---

## Constraints

- `1 <= s.length <= 3 * 10⁵`  
- `s` consist of printable ASCII characters.

---

## Solution Strategy

To solve this problem, I used a **two-pointer swap** approach:

1. **Initialize** a set `vowels` containing all vowels (both cases), convert `s` to a list `res`, and set pointers `l = 0` and `r = len(s) - 1`
2. **Loop** while `l < r`:
   - **Advance `l`** past non-vowel characters from the left
   - **Advance `r`** past non-vowel characters from the right
   - **Swap** `res[l]` and `res[r]`, then move both pointers inward
3. **Return** `''.join(res)`.

### Why This Approach?

The two-pointer technique efficiently reverses only the vowels in-place without affecting consonants:
- **Time Complexity:** O(n) — Each character is visited at most once by each pointer
- **Space Complexity:** O(n) — The list conversion of the string (strings are immutable in Python)

Using a set for vowel lookups gives O(1) membership checks. The left and right pointers converge toward the center, swapping vowels they encounter — consonants remain untouched in their original positions.

---
