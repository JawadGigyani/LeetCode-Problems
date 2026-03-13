# 228. Summary Ranges

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/summary-ranges/description/)

---

## Problem Description

You are given a **sorted unique** integer array `nums`.

A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. Each range `[a,b]` should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

---

## Examples

**Example 1:**

```
Input: nums = [0,1,2,4,5,7]  
Output: ["0->2","4->5","7"]  
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**Example 2:**

```
Input: nums = [0,2,3,4,6,8,9]  
Output: ["0","2->4","6","8->9"]  
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

---

## Constraints

- `0 <= nums.length <= 20`  
- `-2^31 <= nums[i] <= 2^31 - 1`  
- All the values of `nums` are **unique**.  
- `nums` is sorted in ascending order.

---

## Solution Strategy

To solve this problem, I used a **two-pointer range detection** approach:

1. **Initialize** an empty `result` list and pointer `i = 0`
2. **Loop while `i < len(nums)`**:
   - Record the `start` of the current range as `nums[i]`
   - **Extend the range**: while the next element is consecutive (`nums[i] + 1 == nums[i+1]`), advance `i`
   - **Format the range**:
     - If `start != nums[i]` → append `"start->end"`
     - If `start == nums[i]` → append `"start"` (single element)
   - Move `i` forward
3. **Return** `result`.

### Why This Approach?

The inner while loop greedily extends each consecutive range:
- **Time Complexity:** O(n) - Each element is visited exactly once
- **Space Complexity:** O(1) - Excluding the output list

Since the array is sorted and unique, consecutive numbers always form contiguous ranges. The inner loop finds the end of each range, and we format it based on whether it's a single number or a span.

---
