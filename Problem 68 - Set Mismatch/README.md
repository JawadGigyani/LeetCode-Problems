# 645. Set Mismatch

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/set-mismatch/description/)

---

## Problem Description

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one number** and **loss of another number**.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,2,4]  
Output: [2,3]  
Explanation: 2 appears twice and 3 is missing from the set {1, 2, 3, 4}.
```

**Example 2:**

```
Input: nums = [1,1]  
Output: [1,2]  
Explanation: 1 appears twice and 2 is missing from the set {1, 2}.
```

---

## Constraints

- `2 <= nums.length <= 10⁴`  
- `1 <= nums[i] <= 10⁴`

---

## Solution Strategy

To solve this problem, I used a **set-based detection** approach:

1. **Initialize** an empty set `seen` and a variable `duplicate`
2. **Find the duplicate**: Iterate through `nums` — if a number is already in `seen`, it's the duplicate; otherwise add it to `seen`
3. **Find the missing number**: Iterate from `1` to `n` — the first number not in `seen` is the missing one
4. **Return** `[duplicate, missing]`.

### Why This Approach?

Using a set gives O(1) lookups for both duplicate detection and missing number identification:
- **Time Complexity:** O(n) — Two linear passes: one over `nums`, one over `1..n`
- **Space Complexity:** O(n) — The set stores up to n elements

The first pass catches the duplicate via set membership, and the second pass finds the gap in the expected `1..n` sequence. Simple and direct.

---
