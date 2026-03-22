# 390. Elimination Game

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/elimination-game/description/)

---

## Problem Description

You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

1. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
2. Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
3. Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return the last number that remains in `arr`.

---

## Examples

**Example 1:**

```
Input: n = 9  
Output: 6  
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
```

**Example 2:**

```
Input: n = 1  
Output: 1  
```

---

## Constraints

- `1 <= n <= 10⁹`

---

## Solution Strategy

To solve this problem, I used a **recursive simulation** approach that tracks the head of the remaining sequence instead of the full list:

1. **Define a recursive `solve(head, step, length, is_left)`**:
   - `head` — the first element of the current sequence
   - `step` — the gap between consecutive elements
   - `length` — how many elements remain
   - `is_left` — whether this pass goes left-to-right
2. **Base case**: If `length == 1`, return `head` (last remaining number)
3. **Update the head**:
   - **Left-to-right pass**: The first element is always removed, so `head += step`
   - **Right-to-left pass**: The head only shifts if `length` is odd (otherwise the first element survives)
4. **Recurse** with `step * 2` (elements are now spaced twice as far apart), `length // 2`, and the direction flipped
5. **Start** with `solve(1, 1, n, True)`.

### Why This Approach?

Instead of simulating the full array (which would be O(n) per pass), we mathematically track only the head position:
- **Time Complexity:** O(log n) — The length halves each recursion
- **Space Complexity:** O(log n) — Recursion stack depth

Each elimination pass removes half the elements and doubles the spacing. By only tracking the head and deducing when it shifts, we avoid materializing the array entirely — critical since `n` can be up to 10⁹.

---
