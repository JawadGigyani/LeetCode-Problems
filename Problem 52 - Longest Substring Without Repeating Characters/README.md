# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

---

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

---

## Examples

**Example 1:**

```
Input: s = "abcabcbb"  
Output: 3  
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"  
Output: 1  
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"  
Output: 3  
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

---

## Constraints

- `0 <= s.length <= 5 * 10^4`  
- `s` consists of English letters, digits, symbols and spaces.

---

## Solution Strategy

To solve this problem, I used a **sliding window with set comparison** approach:

1. **Initialize** `left = 0`, `right = 0`, and `max_length = 0`
2. **Loop while `right < len(s)`**:
   - Extract the current window: `s[left:right+1]`
   - If all characters are unique (`len(window) == len(set(window))`):
     - Update `max_length` with the window size
     - Expand the window: `right += 1`
   - Otherwise (duplicate found):
     - Shrink the window from the left: `left += 1`
3. **Return** `max_length`.

### Why This Approach?

The sliding window dynamically adjusts to find the longest valid substring:
- **Time Complexity:** O(n²) - Due to creating a set from the window at each step
- **Space Complexity:** O(n) - The set stores up to n unique characters

When all characters in the window are unique, we expand right to try a longer substring. When a duplicate is found, we shrink from the left until uniqueness is restored.

---
