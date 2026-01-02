# 1. Two Sum

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/two-sum/description/)

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

## Examples

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6  
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6  
Output: [0,1]
```

---

## Constraints

- `2 <= nums.length <= 10^4`  
- `-10^9 <= nums[i] <= 10^9`  
- `-10^9 <= target <= 10^9`  
- Only one valid answer exists.

---

## Solution Strategy

To solve this problem, I used a **hash map** approach for optimal performance:

1. **Create an empty dictionary** called `checked` to store numbers we've seen along with their indices.
2. **Iterate through each element** in the array with its index:
   - Calculate the `complement` (the number needed to reach the target): `complement = target - num`
   - If the complement already exists in the dictionary, we've found our pair → return `[checked[complement], i]`
   - Otherwise, store the current number and its index in the dictionary: `checked[num] = i`
3. The problem guarantees exactly one solution, so we'll always find the answer.

### Why This Approach?

Using a hash map allows for **O(1)** average-case lookup time, making this solution very efficient:
- **Time Complexity:** O(n) - We iterate through the array once
- **Space Complexity:** O(n) - In the worst case, we store all elements in the hash map

This is much more efficient than a brute force approach (O(n²)) that would check every pair of numbers.

---
