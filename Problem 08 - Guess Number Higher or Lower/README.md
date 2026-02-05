# 374. Guess Number Higher or Lower

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/guess-number-higher-or-lower/description/)

---

## Problem Description

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`)
- `1`: Your guess is lower than the number I picked (i.e. `num < pick`)
- `0`: Your guess is equal to the number I picked (i.e. `num == pick`)

Return the number that I picked.

---

## Examples

**Example 1:**

```
Input: n = 10, pick = 6  
Output: 6
```

**Example 2:**

```
Input: n = 1, pick = 1  
Output: 1
```

**Example 3:**

```
Input: n = 2, pick = 1  
Output: 1
```

---

## Constraints

- `1 <= n <= 2^31 - 1`  
- `1 <= pick <= n`

---

## Solution Strategy

To solve this problem, I used a **binary search** approach with the provided API:

1. **Initialize two pointers**:
   - `low` starting at 0
   - `high` starting at `n`
2. **Loop while `low <= high`**:
   - Calculate the middle value: `mid = (low + high) // 2`
   - Call the `guess(mid)` API to get the result
   - If `result == 0`, we found the number → return `mid`
   - If `result == -1`, our guess is too high → move `high = mid - 1`
   - If `result == 1`, our guess is too low → move `low = mid + 1`
3. The loop will always find the answer since the picked number is guaranteed to exist.

### Why This Approach?

Binary search is ideal for this guessing game:
- **Time Complexity:** O(log n) - We halve the search space with each guess
- **Space Complexity:** O(1) - We only use a few variables

The `guess()` API essentially acts as our comparator, telling us which direction to search. This is a classic application of binary search where we efficiently narrow down the search range until we find the exact number.

---
