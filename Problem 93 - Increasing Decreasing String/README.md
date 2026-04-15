# 1370. Increasing Decreasing String

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/increasing-decreasing-string/description/)

---

## Problem Description

You are given a string `s`. Reorder the string using the following algorithm:

1. Remove the smallest character from `s` and append it to the result.
2. Remove the smallest character from `s` that is greater than the last appended character, and append it to the result.
3. Repeat step 2 until no more characters can be removed.
4. Remove the largest character from `s` and append it to the result.
5. Remove the largest character from `s` that is smaller than the last appended character, and append it to the result.
6. Repeat step 5 until no more characters can be removed.
7. Repeat steps 1 through 6 until all characters from `s` have been removed.

If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

Return the resulting string after reordering `s` using this algorithm.

---

## Examples

**Example 1:**

```
Input: s = "aaaabbbbcccc"  
Output: "abccbaabccba"  
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
```

**Example 2:**

```
Input: s = "rat"  
Output: "art"  
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
```

---

## Constraints

- `1 <= s.length <= 500`  
- `s` consists of only lowercase English letters.

---

## Solution Strategy

To solve this problem, I used a **character frequency array** approach:

1. **Count Frequencies**: Create an array `freq` of size 26 to store the counts of each character in the string `s`.
2. **Build the Result**: Initialize an empty list `result`.
3. **Loop Until Done**: While the length of `result` is less than the length of `s`, perform a forward and backward pass:
   - **Forward Pass (Increasing)**: Iterate through the alphabet (`0` to `25`). If a character has a frequency `> 0`, append it to `result` and decrement its frequency.
   - **Backward Pass (Decreasing)**: Iterate through the alphabet backwards (`25` down to `0`). If a character has a frequency `> 0`, append it to `result` and decrement its frequency.
4. **Return**: Join the `result` list into a string and return it.

### Why This Approach?

Using a fixed-size frequency array allows us to easily select characters in ascending and descending alphabetical order without needing repeated sorting operations:
- **Time Complexity:** O(N) — Counting frequencies takes O(N). The `while` loop runs at most `N` times, but across all iterations, we check indices at most `26 * (max character frequency)`. Overall, this is linearly bounded by the length of the string.
- **Space Complexity:** O(1) — The frequency array restricts itself to a fixed size of 26 (constant spatial complexity). The extra space required for `result` is strictly equal to the output size constraint.

This approach gracefully handles all duplicates and natively respects the "greater than" / "smaller than" condition by scanning sequentially across the alphabetically ordered tally.

---
