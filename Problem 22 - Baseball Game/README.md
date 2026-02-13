# 682. Baseball Game

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/baseball-game/description/)

---

## Problem Description

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is one of the following:

- An integer `x` - Record a new score of `x`.
- `"+"` - Record a new score that is the sum of the previous two scores.
- `"D"` - Record a new score that is the double of the previous score.
- `"C"` - Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

---

## Examples

**Example 1:**

```
Input: ops = ["5","2","C","D","+"]  
Output: 30  
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
```

**Example 2:**

```
Input: ops = ["5","-2","4","C","D","9","+","+"]  
Output: 27
```

**Example 3:**

```
Input: ops = ["1","C"]  
Output: 0
```

---

## Constraints

- `1 <= operations.length <= 1000`  
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`.  
- For operation `"+"`, there will always be at least two previous scores on the record.  
- For operations `"C"` and `"D"`, there will always be at least one previous score on the record.

---

## Solution Strategy

To solve this problem, I used a **stack-based simulation** approach:

1. **Initialize an empty list** `record` to act as a stack of scores.
2. **Iterate through each operation**:
   - If `"+"` → append the sum of the last two scores (`record[-1] + record[-2]`)
   - If `"D"` → append double the last score (`record[-1] * 2`)
   - If `"C"` → remove the last score (`record.pop()`)
   - Otherwise → convert the string to an integer and append it
3. **Return** the sum of all scores in the record.

### Why This Approach?

A stack naturally models this problem since all operations reference the most recent scores:
- **Time Complexity:** O(n) - We iterate through operations once, plus O(n) for the final sum
- **Space Complexity:** O(n) - The record stack stores up to n scores

Using a list as a stack gives us O(1) access to the last two elements via negative indexing, making each operation efficient.

---
