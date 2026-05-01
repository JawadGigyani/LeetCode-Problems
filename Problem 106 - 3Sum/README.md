# 15. 3Sum

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/3sum/description/)

---

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

---

## Examples

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

---

## Constraints

- `3 <= nums.length <= 3000`
- `-10⁵ <= nums[i] <= 10⁵`

---

## Solution Strategy

To solve this problem, I used a **Sorting + Two Pointers** approach:

1. **Sort** the array `nums` to easily avoid duplicates and enable the two-pointer technique.
2. **Iterate** through the array using index `i` as the first element of our triplet.
   - If the current element is the same as the previous one (`nums[i] == nums[i - 1]`), we **skip** it to avoid duplicate triplets.
3. For each `nums[i]`, **initialize two pointers**:
   - `left` pointing to the element right after `i` (`i + 1`)
   - `right` pointing to the last element of the array (`len(nums) - 1`)
4. **Loop** while `left < right`:
   - Calculate the sum of the three elements: `total = nums[i] + nums[left] + nums[right]`
   - If `total < 0`, the sum is too small, so we increment `left` to increase the sum.
   - If `total > 0`, the sum is too large, so we decrement `right` to decrease the sum.
   - If `total == 0`, we found a valid triplet! Add it to the result `res`.
     - To avoid duplicate triplets with the same `left` and `right` values, we skip over identical elements by incrementing `left` and decrementing `right` until they point to different values.
     - Finally, move both pointers inward to look for other possible pairs.

### Why This Approach?

The two-pointer technique after sorting is highly efficient for subset sum problems.

- **Time Complexity:** O(n²) — Sorting takes O(n log n) and the two-pointer traversal takes O(n) for each of the n elements, dominating the runtime with O(n²).
- **Space Complexity:** O(1) or O(n) — Depending on the language's sorting algorithm implementation (Python's Timsort uses O(n) space). Excluding the space required for output, the logic itself operates with constant extra space.

The key insight is that sorting the array not only allows the two pointers to predictably adjust the sum (move right to decrease, move left to increase) but also clusters identical numbers together, making it trivial to skip duplicates.
