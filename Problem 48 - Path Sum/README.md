# 112. Path Sum

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/path-sum/description/)

---

## Problem Description

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

---

## Examples

**Example 1:**

![Path Sum Example 1](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22  
Output: true  
Explanation: The root-to-leaf path with the target sum is shown.
```

**Example 2:**

![Path Sum Example 2](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5  
Output: false  
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

**Example 3:**

```
Input: root = [], targetSum = 0  
Output: false  
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.  
- `-1000 <= Node.val <= 1000`  
- `-1000 <= targetSum <= 1000`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS with running sum** approach:

1. **Define a helper `dfs(node, box)`** where `box` tracks the cumulative sum
2. **Base case**: If `node` is `None`, return `False`
3. **Add** the current node's value to `box`
4. **Leaf check**: If the node is a leaf (`no left and no right`), return whether `box == targetSum`
5. **Recurse**: Return `dfs(node.left, box) or dfs(node.right, box)`
6. **Start** with `dfs(root, 0)`.

### Why This Approach?

Recursive DFS naturally explores all root-to-leaf paths:
- **Time Complexity:** O(n) - We visit every node in the worst case
- **Space Complexity:** O(h) - Recursion stack depth, where h is the tree height

The running sum `box` accumulates values along each path. At leaf nodes, we check if the total matches `targetSum`. The `or` operator short-circuits — we stop as soon as one valid path is found.

---
