# 100. Same Tree

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/same-tree/description/)

---

## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

---

## Examples

**Example 1:**

![Same Tree Example 1](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]  
Output: true
```

**Example 2:**

![Same Tree Example 2](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]  
Output: false
```

**Example 3:**

![Same Tree Example 3](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]  
Output: false
```

---

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`.  
- `-10^4 <= Node.val <= 10^4`

---

## Solution Strategy

To solve this problem, I used a **recursive comparison** approach:

1. **Base case 1**: If both `p` and `q` are `None`, return `True` (both empty = same)
2. **Base case 2**: If only one is `None`, or their values differ, return `False`
3. **Recurse**: Return `isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`

### Why This Approach?

Recursive comparison elegantly checks both structure and values:
- **Time Complexity:** O(n) - We visit every node in both trees once
- **Space Complexity:** O(h) - Recursion stack depth, where h is the tree height

The solution short-circuits early: if any node pair doesn't match (structurally or by value), it immediately returns `False` without checking the rest of the tree.

---
