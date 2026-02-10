# 344. Reverse String

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/reverse-string/description/)

---

## Problem Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with O(1) extra memory.

---

## Examples

**Example 1:**

```
Input: s = ["h","e","l","l","o"]  
Output: ["o","l","l","e","h"]
```

**Example 2:**

```
Input: s = ["H","a","n","n","a","h"]  
Output: ["h","a","n","n","a","H"]
```

---

## Constraints

- `1 <= s.length <= 10^5`  
- `s[i]` is a printable ASCII character.

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach with in-place swapping:

1. **Initialize two pointers**: `low = 0` and `high = len(s) - 1`
2. **Loop while `low < high`**:
   - **Swap** the characters at `low` and `high`: `s[low], s[high] = s[high], s[low]`
   - Move both pointers inward (`low += 1`, `high -= 1`)
3. The array is modified **in-place** as required by the problem.

### Why This Approach?

The two-pointer swap is the classic way to reverse an array:
- **Time Complexity:** O(n) - We traverse half the array
- **Space Complexity:** O(1) - Only using two pointer variables

By swapping elements from both ends moving inward, we reverse the entire array without needing any extra space.

---
