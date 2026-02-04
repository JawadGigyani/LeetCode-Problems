# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

## Problem Description

Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only **constant extra space**.

---

## Examples

**Example 1:**

```
Input: numbers = [2,7,11,15], target = 9  
Output: [1,2]  
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**

```
Input: numbers = [2,3,4], target = 6  
Output: [1,3]  
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**

```
Input: numbers = [-1,0], target = -1  
Output: [1,2]  
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

---

## Constraints

- `2 <= numbers.length <= 3 * 10^4`  
- `-1000 <= numbers[i] <= 1000`  
- `numbers` is sorted in non-decreasing order.  
- `-1000 <= target <= 1000`  
- The tests are generated such that there is exactly one solution.

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach that leverages the sorted nature of the array:

1. **Initialize two pointers**:
   - `l` (left) pointing to the start of the array (index 0)
   - `r` (right) pointing to the end of the array (index `len(numbers) - 1`)
2. **Loop while left pointer is less than right pointer**:
   - Calculate `curr_sum = numbers[l] + numbers[r]`
   - If `curr_sum == target`, we found our answer → return `[l+1, r+1]` (1-indexed)
   - If `curr_sum < target`, move the left pointer right (`l += 1`) to increase the sum
   - If `curr_sum > target`, move the right pointer left (`r -= 1`) to decrease the sum
3. The problem guarantees exactly one solution, so we'll always find the answer.

### Why This Approach?

The two-pointer technique is perfect for sorted arrays:
- **Time Complexity:** O(n) - We traverse the array at most once
- **Space Complexity:** O(1) - We only use two pointer variables

Since the array is sorted, moving the left pointer increases the sum while moving the right pointer decreases it. This allows us to efficiently narrow down to the target sum without needing extra space (unlike the hash map approach in regular Two Sum).

---
