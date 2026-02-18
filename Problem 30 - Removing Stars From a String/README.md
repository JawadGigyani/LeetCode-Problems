# 2390. Removing Stars From a String

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/removing-stars-from-a-string/description/)

---

## Problem Description

You are given a string `s`, which contains stars `*`.

In one operation, you can:

- Choose a star in `s`.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

---

## Examples

**Example 1:**

```
Input: s = "leet**cod*e"  
Output: "lecoe"  
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
```

**Example 2:**

```
Input: s = "erase*****"  
Output: ""  
Explanation: The entire string is removed, so we return an empty string.
```

---

## Constraints

- `1 <= s.length <= 10^5`  
- `s` consists of lowercase English letters and stars `*`.  
- The operation above can be performed on `s`.

---

## Solution Strategy

To solve this problem, I used a **stack-based** approach:

1. **Initialize an empty stack** (list)
2. **Iterate through each character** in the string:
   - If the character is `"*"`, pop the top element from the stack (removes the closest non-star character)
   - Otherwise, push the character onto the stack
3. **Return** the stack joined as a string: `"".join(stack)`

### Why This Approach?

A stack naturally handles the "remove closest to the left" logic:
- **Time Complexity:** O(n) - We traverse the string once
- **Space Complexity:** O(n) - The stack stores up to n characters

Each star acts as a "backspace" that removes the most recently added character. The stack's LIFO nature perfectly models this behavior, making the solution clean and efficient.

---
