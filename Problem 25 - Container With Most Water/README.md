# 11. Container With Most Water

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/container-with-most-water/description/)

---

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i<sup>th</sup> line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

---

## Examples

**Example 1:**

![Container With Most Water](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]  
Output: 49  
Explanation: The max area of water the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]  
Output: 1
```

---

## Constraints

- `n == height.length`  
- `2 <= n <= 10^5`  
- `0 <= height[i] <= 10^4`

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach:

1. **Initialize two pointers**: `left = 0` and `right = len(height) - 1`
2. **Initialize** `max_area = 0` to track the maximum water area
3. **Loop while `left < right`**:
   - Calculate the area: `min(height[left], height[right]) * (right - left)`
   - Update `max_area` if the current area is larger
   - **Move the shorter line's pointer inward**:
     - If `height[left] < height[right]`, move `left += 1`
     - Otherwise, move `right -= 1`
4. **Return** the `max_area`.

### Why This Approach?

The two-pointer technique greedily maximizes the container area:
- **Time Complexity:** O(n) - We traverse the array once
- **Space Complexity:** O(1) - Only using pointer variables

The key insight is that we always move the pointer with the shorter height. The area is limited by the shorter line, so keeping the taller line and trying a new shorter line is the only way to potentially find a larger area. Moving the taller line would only decrease or maintain the width while the height can't improve.

---
