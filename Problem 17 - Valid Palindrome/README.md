# 125. Valid Palindrome

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/valid-palindrome/description/)

---

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Examples

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"  
Output: true  
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"  
Output: false  
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**

```
Input: s = " "  
Output: true  
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

---

## Constraints

- `1 <= s.length <= 2 * 10^5`  
- `s` consists only of printable ASCII characters.

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach with in-place filtering:

1. **Initialize two pointers**: `left = 0` and `right = len(s) - 1`
2. **Loop while `left < right`**:
   - **Skip non-alphanumeric characters** from the left using `isalnum()`
   - **Skip non-alphanumeric characters** from the right using `isalnum()`
   - **Compare characters** (case-insensitive using `lower()`):
     - If they don't match, return `False`
   - Move both pointers inward (`left += 1`, `right -= 1`)
3. If the loop completes, return `True` (it's a valid palindrome).

### Why This Approach?

The two-pointer technique avoids creating a filtered string copy:
- **Time Complexity:** O(n) - We traverse the string once
- **Space Complexity:** O(1) - No extra space needed (only pointers)

By skipping non-alphanumeric characters on-the-fly and comparing case-insensitively, we efficiently validate the palindrome without preprocessing the string.

---
