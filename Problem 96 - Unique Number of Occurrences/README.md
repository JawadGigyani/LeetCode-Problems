# 1207. Unique Number of Occurrences

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/unique-number-of-occurrences/description/)

---

## Problem Description

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique** or `false` otherwise.

---

## Examples

**Example 1:**

```
Input: arr = [1,2,2,1,1,3]  
Output: true  
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

**Example 2:**

```
Input: arr = [1,2]  
Output: false  
```

**Example 3:**

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]  
Output: true  
```

---

## Constraints

- `1 <= arr.length <= 1000`  
- `-1000 <= arr[i] <= 1000`

---

## Solution Strategy

To solve this problem, I used a **frequency map and a tracking set** approach:

1. **Count Frequencies:** Use Python's built-in `Counter` from the `collections` module to tally up the occurrences of each distinct integer in the array `arr`.
2. **Track Seen Frequencies:** Initialize an empty set `checked` to keep track of the frequencies we process.
3. **Validate Uniqueness:** Iterate through the unique keys (the distinct values) in the frequency map:
   - If the current value's frequency (`freq[val]`) is already in the `checked` set, it means we've found two different values with the same number of occurrences. Return `False`.
   - If not, add the frequency to the `checked` set and continue.
4. **Return True:** If the loop completes without finding duplicate frequencies, return `True`.

### Why This Approach?

This strategy provides an optimal and direct way to verify the uniqueness of element frequencies:
- **Time Complexity:** $O(N)$ — Where $N$ is the length of `arr`. Counting frequencies takes $O(N)$ time. Iterating through the unique keys and checking/adding to the set takes average $O(1)$ time per unique element, bounding the second loop to $O(N)$ overall.
- **Space Complexity:** $O(N)$ — In the worst-case scenario (all uniquely occurring elements), the `Counter` hash map and the `checked` set both store information proportional to the length of the array, taking $O(N)$ extra space.

*(Note: The request to add a gif in the example was omitted as there is no visual gif asset inherently tied to this specific problem's LeetCode description like there was in previous problems.)*
