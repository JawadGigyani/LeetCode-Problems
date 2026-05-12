# 1544. Make The String Great

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/make-the-string-great/description/)

---

## Problem Description

You are given a string `s` consisting of lower‑case and upper‑case English letters.

A **good** string is one that **does not** contain any adjacent pair of characters `s[i]` and `s[i+1]` where one is the lower‑case version of a letter and the other is the same letter in upper‑case (or vice‑versa).

To make the string good, you may repeatedly choose a *bad* adjacent pair and delete both characters. Continue this process until the string becomes good. The result is guaranteed to be unique.

Return the final good string. An empty string is considered good.

---

## Examples

**Example 1:**

```text
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: The pair "eE" (or "Ee") can be removed first, leaving "leetcode" which is already good.
```

**Example 2:**

```text
Input: s = "abBAcC"
Output: ""
Explanation: No matter which adjacent opposite‑case pairs you delete, the process always ends with an empty string.
```

**Example 3:**

```text
Input: s = "s"
Output: "s"
```

---

## Constraints

- `1 <= s.length <= 100`
- `s` contains only English letters (`a‑z`, `A‑Z`).

---

## Solution Strategy

The problem is naturally solved with a **stack** that simulates the cancellation process:

1. Initialise an empty list `stack`.
2. Iterate over each character `ch` in `s`:
   - If the stack is non‑empty **and** the top element `stack[-1]` forms a bad pair with `ch` (their ASCII codes differ by exactly `32`, i.e., `abs(ord(stack[-1]) - ord(ch)) == 32`), pop the top element – the pair annihilates.
   - Otherwise, push `ch` onto the stack.
3. After processing the entire string, the stack holds the characters of the good string in order. Join them with `''.join(stack)` and return.

### Why This Works

- The stack always stores the current *partial* good string. When a new character arrives, it only needs to be compared with the most recent character because any earlier conflict would already have been resolved.
- Deleting a pair never creates a new conflict with characters further left than the popped element, preserving correctness.
- The algorithm is linear because each character is pushed at most once and popped at most once.

---

## Complexity Analysis

- **Time Complexity:** `O(n)` where `n = len(s)`. Each character is examined a constant number of times.
- **Space Complexity:** `O(n)` in the worst case (when the string is already good), storing the entire result on the stack.

---
