# 844. Backspace String Compare

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/backspace-string-compare/description/)

---

## Problem Description

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

---

## Examples

**Example 1:**

```
Input: s = "ab#c", t = "ad#c"  
Output: true  
Explanation: Both s and t become "ac".
```

**Example 2:**

```
Input: s = "ab##", t = "c#d#"  
Output: true  
Explanation: Both s and t become "".
```

**Example 3:**

```
Input: s = "a#c", t = "b"  
Output: false  
Explanation: s becomes "c" while t becomes "b".
```

---

## Constraints

- `1 <= s.length, t.length <= 200`  
- `s` and `t` only contain lowercase letters and `'#'` characters.

---

## Solution Strategy

To solve this problem, I used a **stack-based builder** approach with a helper function:

1. **Define a helper function `build(st)`**:
   - Initialize an empty stack
   - Iterate through each character:
     - If `'#'`, pop from the stack (if not empty) — simulates backspace
     - Otherwise, push the character onto the stack
   - Return the stack joined as a string
2. **Compare** the built strings: `build(s) == build(t)`

### Why This Approach?

Using a reusable helper function keeps the code clean and DRY:
- **Time Complexity:** O(n + m) - Where n and m are the lengths of `s` and `t`
- **Space Complexity:** O(n + m) - The stacks store up to n and m characters

The stack naturally handles backspace behavior — each `'#'` removes the most recently typed character. The extra `if stack` check before popping prevents errors when backspacing an already empty text.

---
