# 1047. Remove All Adjacent Duplicates In String

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)

---

## Problem Description

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

---

## Examples

**Example 1:**

```text
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

**Example 2:**

```text
Input: s = "azxxzy"
Output: "ay"
```

---

## Constraints

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.

---

## Solution Strategy

This problem is perfectly suited for a **stack** data structure, which allows us to process the string character by character while keeping track of the most recently unmatched characters:

1. Initialise an empty list `stack`.
2. Iterate through each character `ch` in the string `s`:
   - If the stack is **not empty** and the top element of the stack (`stack[-1]`) is exactly the same as the current character `ch`, it means we've found an adjacent duplicate pair. We **pop** the top element from the stack to "remove" the pair.
   - If the stack is empty or the top character does not match, we **push** the current character `ch` onto the stack.
3. Once the iteration is complete, the `stack` contains all the characters that couldn't be paired up and removed. We join the stack into a string (`''.join(stack)`) and return it.

### Why This Works

- The stack acts as a memory of the previously seen, unpaired characters. By only comparing the current character with the *top* of the stack, we efficiently check for adjacent duplicates. 
- When a pair is removed, the characters that were on either side of the pair automatically become adjacent. The stack handles this seamlessly, as the new "top" element naturally exposes the character that was immediately before the removed pair.

## Complexity Analysis

- **Time Complexity:** `O(n)` where `n = len(s)`. We iterate through the string exactly once. Both pushing to and popping from a stack (list in Python) are `O(1)` operations on average. Joining the list at the end is also `O(n)`.
- **Space Complexity:** `O(n)` in the worst case (e.g., if there are no adjacent duplicates, like "abcdef"), as we store all characters in the stack.
