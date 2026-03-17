# 129. Sum Root to Leaf Numbers

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

---

## Problem Description

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number. For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. A **leaf** node is a node with no children.

---

## Examples

**Example 1:**

![Sum Root to Leaf Example 1](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

```
Input: root = [1,2,3]  
Output: 25  
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:**

![Sum Root to Leaf Example 2](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

```
Input: root = [4,9,0,5,1]  
Output: 1026  
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.  
- `0 <= Node.val <= 9`  
- The depth of the tree will not exceed `10`.

---

## Solution Strategy

To solve this problem, I used a **recursive DFS with string path building** approach:

1. **Initialize** an empty list `self.result` to store number strings
2. **Define a recursive `dfs(node, path)`**:
   - If `node` is `None`, return
   - **Append** the current node's digit to the string `path`
   - **Leaf check**: If the node is a leaf, append the full `path` string to `self.result`
   - **Recurse** on left and right children
3. **Run** `dfs(root, "")`
4. **Sum the values**: Convert each string in `self.result` to an integer with `int(i)` and accumulate the total
5. **Return** the total sum.

### Why This Approach?

DFS with string concatenation cleanly builds decimal numbers along each path:
- **Time Complexity:** O(n * h) - We visit every node, string concatenation takes O(h) per node
- **Space Complexity:** O(n * h) - Storing all path strings, plus recursion stack

Similar to the binary version (Problem 64), but here we use `int(i)` instead of `int(i, 2)` since nodes contain decimal digits (0–9) rather than binary digits.

---
