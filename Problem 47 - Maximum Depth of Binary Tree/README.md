# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

---

## Problem Description

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Examples

**Example 1:**

![Maximum Depth Example 1](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]  
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]  
Output: 2
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.  
- `-100 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS** approach:

1. **Base case**: If `root` is `None`, return `0`
2. **Recurse** on both subtrees:
   - `left_depth = maxDepth(root.left)`
   - `right_depth = maxDepth(root.right)`
3. **Return** `1 + max(left_depth, right_depth)` — current node plus the deeper subtree.

### Why This Approach?

Recursive depth calculation is the most natural solution for tree problems:
- **Time Complexity:** O(n) - We visit every node exactly once
- **Space Complexity:** O(h) - Recursion stack depth, where h is the tree height

Each node contributes 1 to the depth, and we always take the path through the deeper subtree. The recursion bottoms out at `None` nodes (depth 0) and builds up the answer.

---
