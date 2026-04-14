# 1832. Check if the Sentence Is Pangram

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/)

---

## Problem Description

A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return `true` if `sentence` is a pangram, or `false` otherwise.

---

## Examples

**Example 1:**

```
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"  
Output: true  
Explanation: sentence contains at least one of every letter of the English alphabet.
```

**Example 2:**

```
Input: sentence = "leetcode"  
Output: false  
```

---

## Constraints

- `1 <= sentence.length <= 1000`  
- `sentence` consists of lowercase English letters.

---

## Solution Strategy

To solve this problem, I have provided two different approaches:

### Solution 1: Frequency Array using ASCII Offsets

This approach uses a fixed-size array to track letter occurrences:

1. **Initialize** an array `freq` of size 26 filled with `0`s.
2. **Iterate** through each character in the `sentence`:
   - Calculate its index `0-25` using its ASCII value (`ord(alph) - 97`) since 'a' is 97.
   - Increment the count at that index.
3. **Verify**: If there is any `0` left in the `freq` array, it means a letter is missing, so return `False`. Otherwise, return `True`.

**Complexity:**
- **Time Complexity:** O(N) — Single pass through the string of length N.
- **Space Complexity:** O(1) — The frequency array always takes exactly size 26, independent of string length. *(Note: The current implementation casts the string to a list which takes O(N) space, but iterating directly over the string would use O(1) space).*

### Solution 2: Python Set Length Check

This approach leverages Python's built-in set data structure to find unique characters:

1. **Convert** the `sentence` into a `set()`. This automatically removes all duplicate characters, leaving only the unique letters present.
2. **Check Length**: Return `True` if the length of this set is exactly `26` (the number of letters in the English alphabet), else `False`.

**Complexity:**
- **Time Complexity:** O(N) — Hashing the string characters into a set takes linear time.
- **Space Complexity:** O(1) — The set can store a maximum of 26 unique lowercase English letters, taking constant extra space regardless of the input string length.

### Comparison

- **Solution 2** is generally preferred in Python due to its extreme conciseness (a one-liner) and taking advantage of optimized built-in data structures (`set`). It directly answers "are there 26 unique characters?" without manual indexing.
- **Solution 1** is a more classical, language-agnostic approach. It demonstrates how to manually map characters to indices using ASCII values, which is an important fundamental concept, especially useful in lower-level languages where dynamic sets aren't available by default.

---
