# 1768. Merge Strings Alternately

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/merge-strings-alternately/description/)

---

## Problem Description

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

---

## Examples

**Example 1:**

```
Input: word1 = "abc", word2 = "pqr"  
Output: "apbqcr"  
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

**Example 2:**

```
Input: word1 = "ab", word2 = "pqrs"  
Output: "apbqrs"  
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
```

**Example 3:**

```
Input: word1 = "abcd", word2 = "pq"  
Output: "apbqcd"  
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
```

---

## Constraints

- `1 <= word1.length, word2.length <= 100`  
- `word1` and `word2` consist of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **two-pointer interleave** approach:

1. **Initialize** two pointers `i = j = 0` and an empty list `output_word`
2. **Loop** while either pointer hasn't reached the end of its string:
   - If `i < len(word1)`, append `word1[i]` and increment `i`
   - If `j < len(word2)`, append `word2[j]` and increment `j`
3. **Return** `''.join(output_word)`.

### Why This Approach?

The two-pointer technique naturally handles both equal and unequal length strings in a single loop:
- **Time Complexity:** O(n + m) — Where n and m are the lengths of `word1` and `word2`
- **Space Complexity:** O(n + m) — The output list stores all characters from both strings

Both pointers advance together during the overlapping portion, producing the alternating pattern. Once the shorter string is exhausted, the remaining characters of the longer string are appended seamlessly — no special handling needed.

---
