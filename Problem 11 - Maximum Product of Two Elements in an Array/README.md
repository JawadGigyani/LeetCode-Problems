# 1464. Maximum Product of Two Elements in an Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/)

---

## Problem Description

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`.

---

## Examples

**Example 1:**

```
Input: nums = [3,4,5,2]  
Output: 12  
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
```

**Example 2:**

```
Input: nums = [1,5,4,5]  
Output: 16  
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
```

**Example 3:**

```
Input: nums = [3,7]  
Output: 12
```

---

## Constraints

- `2 <= nums.length <= 500`  
- `1 <= nums[i] <= 10^3`

---

## Solution Strategy

To solve this problem, I used a **sorting** approach:

1. **Sort the array** in ascending order using `nums.sort()`
2. **Get the two largest elements**:
   - `nums[-1]` is the largest element
   - `nums[-2]` is the second largest element
3. **Calculate and return** the product: `(nums[-1] - 1) * (nums[-2] - 1)`

### Why This Approach?

To maximize the product `(nums[i]-1) * (nums[j]-1)`, we need the two largest values in the array (since all values are positive):
- **Time Complexity:** O(n log n) - Due to the sorting operation
- **Space Complexity:** O(1) - Sorting is done in-place

Sorting gives us easy access to the largest elements via negative indexing. An alternative O(n) approach would track the two largest values in a single pass, but the sorting approach is clean and readable for this problem's constraints.

---
