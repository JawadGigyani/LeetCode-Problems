# 451. Sort Characters By Frequency

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/sort-characters-by-frequency/description/)

---

## Problem Description

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

---

## Examples

**Example 1:**

```
Input: s = "tree"  
Output: "eert"  
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:**

```
Input: s = "cccaaa"  
Output: "aaaccc"  
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:**

```
Input: s = "Aabb"  
Output: "bbAa"  
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

---

## Constraints

- `1 <= s.length <= 5 * 10⁵`  
- `s` consists of uppercase and lowercase English letters and digits.

---

## Solution Strategy

To solve this problem, I used a **frequency counting with sorted reconstruction** approach:

1. **Count Frequencies**: Use `Counter(s)` to build a frequency map of all characters in the string.
2. **Sort by Frequency**: Sort the frequency map items in **descending order** by count using `sorted()` with a lambda key `lambda x: x[1]` and `reverse=True`.
3. **Build the Result**: Iterate through the sorted pairs `(char, count)` and append `char * count` (the character repeated by its frequency) to a result list.
4. **Return**: Join the result list into a string with `''.join(s_list)`.

### Why This Approach?

Sorting the frequency pairs directly gives us the correct character ordering in one step:
- **Time Complexity:** O(n + k log k) — Counting takes O(n), sorting the k unique characters takes O(k log k), and building the result takes O(n). Since k ≤ n, this simplifies to O(n log n) in the worst case.
- **Space Complexity:** O(n) — The frequency map and result list both scale with the input size.

Using `char * count` to repeat characters is a clean Pythonic way to group identical characters together, which satisfies the constraint that same characters must appear adjacent in the output.

---
