# 39. Combination Sum

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/combination-sum/description/)

---

## Problem Description

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

---

## Examples

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7  
Output: [[2,2,3],[7]]  
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8  
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```
Input: candidates = [2], target = 1  
Output: []
```

---

## Constraints

- `1 <= candidates.length <= 30`  
- `2 <= candidates[i] <= 40`  
- All elements of `candidates` are **distinct**.  
- `1 <= target <= 40`

---

## Solution Strategy

To solve this problem, I used a **recursive backtracking** approach:

1. **Initialize** an empty `result` list
2. **Define `backtrack(index, current, remaining)`**:
   - If `remaining == 0`, append a **copy** of `current` to `result` (valid combination found)
   - If `remaining < 0`, return (overshot the target)
   - **Loop from `index`** to end of candidates:
     - Append `candidates[i]` to `current`
     - Recurse with `backtrack(i, current, remaining - candidates[i])` — pass `i` (not `i+1`) to allow reuse
     - **Backtrack**: pop the last element
3. **Start** with `backtrack(0, [], target)` and **return** `result`.

### Why This Approach?

Backtracking explores all valid combinations while pruning invalid paths:
- **Time Complexity:** O(n^(t/m)) - Where t is target and m is the minimum candidate value
- **Space Complexity:** O(t/m) - Maximum recursion depth

The key detail is passing `i` (not `i+1`) in the recursive call, allowing the same candidate to be chosen multiple times. Starting the loop from `index` prevents generating duplicate combinations in different orders.

---
