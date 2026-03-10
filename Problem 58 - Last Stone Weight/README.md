# 1046. Last Stone Weight

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/last-stone-weight/description/)

---

## Problem Description

You are given an array of integers `stones` where `stones[i]` is the weight of the i<sup>th</sup> stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.

---

## Examples

**Example 1:**

```
Input: stones = [2,7,4,1,8,1]  
Output: 1  
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the last stone.
```

**Example 2:**

```
Input: stones = [1]  
Output: 1
```

---

## Constraints

- `1 <= stones.length <= 30`  
- `1 <= stones[i] <= 1000`

---

## Solution Strategy

To solve this problem, I used a **max heap (simulated with negation)** approach:

1. **Negate all values** to simulate a max heap (Python's `heapq` is a min heap): `[-stone for stone in stones]`
2. **Heapify** the list
3. **Loop while more than 1 stone remains**:
   - Pop the two heaviest stones (`y` and `x`)
   - If they're not equal, push the difference `y - x` back onto the heap
4. **Return** the last stone's weight (negated back), or `0` if the heap is empty.

### Why This Approach?

A max heap efficiently retrieves the two heaviest stones each round:
- **Time Complexity:** O(n log n) - Each pop/push is O(log n), up to n rounds
- **Space Complexity:** O(n) - The heap stores all stones

Since Python only has a min heap, we negate values to simulate max heap behavior. The difference `y - x` (both negative) correctly gives the negative of the remaining weight.

---
