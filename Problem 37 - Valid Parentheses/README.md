# 20. Valid Parentheses

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/valid-parentheses/description/)

---

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

---

## Examples

**Example 1:**

```
Input: s = "()"  
Output: true
```

**Example 2:**

```
Input: s = "()[]{}"  
Output: true
```

**Example 3:**

```
Input: s = "(]"  
Output: false
```

**Example 4:**

```
Input: s = "([])"  
Output: true
```

**Example 5:**

```
Input: s = "([)]"  
Output: false
```

---

## Constraints

- `1 <= s.length <= 10^4`  
- `s` consists of parentheses only `'()[]{}'`.

---

## Solution Strategy

To solve this problem, I used a **stack with hash map** approach:

1. **Initialize an empty stack** and a **mapping** of closing brackets to their corresponding opening brackets
2. **Iterate through each character**:
   - If it's a **closing bracket** (found in the mapping):
     - If the stack is empty, return `False` (no matching opener)
     - Pop the top of the stack and check if it matches the expected opening bracket
     - If not, return `False`
   - Otherwise (it's an **opening bracket**):
     - Push it onto the stack
3. **Return** whether the stack is empty — if empty, all brackets were matched.

### Why This Approach?

A stack naturally enforces correct nesting order:
- **Time Complexity:** O(n) - We traverse the string once
- **Space Complexity:** O(n) - The stack stores up to n/2 opening brackets

The hash map provides O(1) lookup for matching bracket pairs. The stack ensures that brackets are closed in the correct order — the most recently opened bracket must be closed first (LIFO).

---
