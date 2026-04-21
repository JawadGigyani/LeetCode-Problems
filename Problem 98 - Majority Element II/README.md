# 229. Majority Element II

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/majority-element-ii/description/)

---

## Problem Description

Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times.

---

## Examples

**Example 1:**

```
Input: nums = [3,2,3]  
Output: [3]  
```

**Example 2:**

```
Input: nums = [1]  
Output: [1]  
```

**Example 3:**

```
Input: nums = [1,2]  
Output: [1,2]  
```

---

## Constraints

- `1 <= nums.length <= 5 * 10⁴`  
- `-10⁹ <= nums[i] <= 10⁹`

---

## Solution Strategy

To solve this problem optimally in linear time and $O(1)$ space, I used the **Boyer-Moore Majority Vote Algorithm (Extended)**:

Since we are looking for elements that appear **more than `⌊n / 3⌋`** times, there can be at most **two** such elements. Therefore, we only need to track two potential candidates.

1. **Initialize Tracking Variables:** Maintain two candidates (`candidate1`, `candidate2`) and their respective counts (`count1`, `count2`), initially set to `None` and `0`.
2. **First Pass (Find Candidates):** Iterate through each number `num` in the array:
   - If `num` matches `candidate1`, increment `count1`.
   - If `num` matches `candidate2`, increment `count2`.
   - If `count1` is `0`, assign `num` as the new `candidate1` and set `count1` to `1`.
   - If `count2` is `0`, assign `num` as the new `candidate2` and set `count2` to `1`.
   - If `num` matches neither candidate and both counts are greater than zero, decrement both `count1` and `count2`.
3. **Second Pass (Validate Candidates):** Because the extended Boyer-Moore algorithm only guarantees that the tracked candidates are the *most likely* majority elements, we must do a second pass to verify if their actual frequency strictly exceeds `⌊n / 3⌋`.
   - Count the total occurrences of `candidate1` and `candidate2` in the array.
   - If a candidate's count `> len(nums) // 3`, append it to the result list.
4. **Return Result:** Return the list of validated majority elements.

### Why This Approach?

This is the most optimal approach for finding threshold-based majority elements:
- **Time Complexity:** $O(n)$ — The array is traversed exactly twice (once to find candidates, once to validate them), keeping the time complexity strictly linear.
- **Space Complexity:** $O(1)$ — Only four tracking variables and a maximum two-element result list are used, independent of the input array size.

This avoids the $O(n)$ space requirement of using a hash map to count all frequencies, completely fulfilling the optimal requirements for this algorithm sub-class.
