# 1160. Find Words That Can Be Formed by Characters

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/)

---

## Problem Description

You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from `chars` (each character can only be used once for each word in `words`).

Return the sum of lengths of all good strings in `words`.

---

## Examples

**Example 1:**

```
Input: words = ["cat","bt","hat","tree"], chars = "atach"  
Output: 6  
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```

**Example 2:**

```
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"  
Output: 10  
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```

---

## Constraints

- `1 <= words.length <= 1000`  
- `1 <= words[i].length, chars.length <= 100`  
- `words[i]` and `chars` consist of lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **frequency counting** approach using Python's `Counter`:

1. **Count Available Characters:** First, create a `Counter` for the string `chars` to track the frequency of each available character. Let's call this `char_count`.
2. **Iterate Through Words:** For each `word` in the `words` array:
   - Create a `Counter` for the current word, `word_count`.
   - Iterate through each unique character `ch` in `word_count`.
   - Check if the required count for `ch` in `word_count` exceeds the available count in `char_count`.
   - If it does, `break` the loop (the word cannot be formed).
   - If the loop finishes without breaking (using Python's `for...else` construct), it means the word can be completely formed. Add its length to a running `total_len` sum.
3. **Return** the `total_len`.

### Why This Approach?

Using frequency hash maps (`Counter`) is the most direct way to verify "subset" relationships between two pools of characters:
- **Time Complexity:** O(N + M) — where `N` is the total number of characters across all `words`, and `M` is the length of `chars`. We count `chars` once, and then count characters for each word, checking against the master pool.
- **Space Complexity:** O(1) — the space used by the `Counter` structures is limited to the alphabet size (at most 26 lowercase English letters), which scales constantly regardless of the input size.

The `for...else` construct in Python pairs perfectly here, seamlessly executing the length addition only when no "missing character" break condition is hit.

---
