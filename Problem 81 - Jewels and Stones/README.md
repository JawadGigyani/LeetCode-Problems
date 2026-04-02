# 771. Jewels and Stones

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/jewels-and-stones/description/)

---

## Problem Description

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

---

## Examples

**Example 1:**

```
Input: jewels = "aA", stones = "aAAbbbb"  
Output: 3  
Explanation: 'a' appears 1 time and 'A' appears 2 times in stones, totaling 3 jewels.
```

**Example 2:**

```
Input: jewels = "z", stones = "ZZ"  
Output: 0  
Explanation: 'z' is not found in stones (case sensitive), so the count is 0.
```

---

## Constraints

- `1 <= jewels.length, stones.length <= 50`  
- `jewels` and `stones` consist of only English letters.  
- All the characters of `jewels` are unique.

---

## Solution Strategy

To solve this problem, I used a **frequency counting** approach:

1. **Count** the frequency of each character in `stones` using `Counter`
2. **Initialize** `count = 0`
3. **Iterate** through each character in `jewels`:
   - If the jewel character exists in the frequency map, add its count to `count`
4. **Return** `count`.

### Why This Approach?

Using `Counter` pre-computes stone frequencies, making jewel lookups efficient:
- **Time Complexity:** O(j + s) — Where j is the length of `jewels` and s is the length of `stones`
- **Space Complexity:** O(s) — The frequency map stores at most s distinct characters

By counting stone frequencies upfront, each jewel type lookup and accumulation is O(1). This avoids the O(j × s) cost of checking each jewel against every stone character directly.

---
