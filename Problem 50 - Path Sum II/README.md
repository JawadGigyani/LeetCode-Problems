# 113. Path Sum II

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/path-sum-ii/description/)

---

## Problem Description

Given the `root` of a binary tree and an integer `targetSum`, return all **root-to-leaf** paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

A **leaf** is a node with no children.

---

## Examples

**Example 1:**

![Path Sum II Example 1](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22  
Output: [[5,4,11,2],[5,8,4,5]]  
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```

**Example 2:**

![Path Sum II Example 2](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5  
Output: []
```

**Example 3:**

```
Input: root = [1,2], targetSum = 0  
Output: []
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.  
- `-1000 <= Node.val <= 1000`  
- `-1000 <= targetSum <= 1000`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS with backtracking** approach:

1. **Initialize** an empty `result` list
2. **Define `dfs(node, current_path, current_sum)`**:
   - Base case: if `node` is `None`, return
   - **Append** the node's value to `current_path` and add to `current_sum`
   - **Leaf check**: if leaf node and `current_sum == targetSum`, append a **copy** of `current_path` to `result`
   - **Recurse** on left and right children
   - **Backtrack**: pop the last element from `current_path`
3. **Start** with `dfs(root, [], 0)` and **return** `result`.

### Why This Approach?

DFS with backtracking efficiently explores all paths while reusing memory:
- **Time Complexity:** O(n²) - We visit every node, and copying a path takes O(n) in the worst case
- **Space Complexity:** O(h) - Recursion stack and current path depth, where h is the tree height

The key technique is **backtracking** — after exploring a subtree, we pop the last node from `current_path` to restore the state for the next branch. Using `.copy()` when saving a valid path is essential since the list is modified in place.

---
