# 2000. Reverse Prefix of Word

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/reverse-prefix-of-word/description/)

---

## Problem Description

Given a **0-indexed** string `word` and a character `ch`, **reverse the segment of word** that starts at index `0` and ends at the index of the **first occurrence** of `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

- For example, if `word = "abcdefd"` and `ch = "d"`, then you should reverse the segment that starts at `0` and ends at `3` (inclusive). The resulting string will be `"dcbaefd"`.

Return the *resulting string*.

---

## Examples

**Example 1:**

```
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
```

**Example 2:**

```
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
```

**Example 3:**

```
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".
```

---

## Constraints

- `1 <= word.length <= 250`
- `word` consists of lowercase English letters.
- `ch` is a lowercase English letter.

---

## Solution Strategy

To solve this problem efficiently in Python, I utilized **built-in string methods and slicing**:

1. **Find Index:** Use `word.find(ch)` to locate the index of the first occurrence of `ch`.
2. **Check Existence:** If `ch` is not found, `find()` returns `-1`. In this case, simply return the original `word`.
3. **Reverse and Concatenate:** 
   - Slice the string up to and including the index: `word[:idx+1]`
   - Reverse this prefix using Python's slice stepping: `[::-1]`
   - Concatenate it with the remainder of the word: `word[idx+1:]`

### Why This Approach?

Python's built-in string operations are implemented in C and are heavily optimized, making this approach extremely concise and fast. 

- **Time Complexity:** O(n) — Searching for the character takes O(n) time. Slicing and reversing also take O(n) time, where `n` is the length of the string. The overall time complexity remains linear.
- **Space Complexity:** O(n) — Strings in Python are immutable, so slicing and concatenating creates a new string of length `n`, requiring O(n) extra space.
