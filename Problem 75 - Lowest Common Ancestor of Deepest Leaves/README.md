# 1123. Lowest Common Ancestor of Deepest Leaves

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/)

---

## Problem Description

Given the `root` of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

- The node of a binary tree is a **leaf** if and only if it has no children.
- The **depth** of the root of the tree is `0`. If the depth of a node is `d`, the depth of each of its children is `d + 1`.
- The **lowest common ancestor** of a set `S` of nodes, is the node `A` with the largest depth such that every node in `S` is in the subtree with root `A`.

---

## Examples

**Example 1:**

![LCA Deepest Leaves Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]  
Output: [2,7,4]  
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2,
but the depth of nodes 7 and 4 is 3.
```

**Example 2:**

```
Input: root = [1]  
Output: [1]  
Explanation: The root is the deepest node in the tree, and it's the LCA of itself.
```

**Example 3:**

```
Input: root = [0,1,3,null,2]  
Output: [2]  
Explanation: The deepest leaf node in the tree is 2, the LCA of one node is itself.
```

---

## Constraints

- The number of nodes in the tree will be in the range `[1, 1000]`.  
- `0 <= Node.val <= 1000`  
- The values of the nodes in the tree are unique.

---

## Solution Strategy

To solve this problem, I used a **post-order DFS returning (node, depth) pairs** approach:

1. **Define a recursive `dfs(node)`** that returns a tuple `(lca_node, depth)`:
   - If `node` is `None`, return `(None, 0)`
   - **Recurse** on left and right children to get `(left_node, left_depth)` and `(right_node, right_depth)`
   - **If `left_depth > right_depth`**: All deepest leaves are on the left side — return `(left_node, left_depth + 1)`
   - **If `right_depth > left_depth`**: All deepest leaves are on the right side — return `(right_node, right_depth + 1)`
   - **If depths are equal**: Deepest leaves exist on both sides — the current `node` is their LCA, so return `(node, right_depth + 1)`
2. **Return** `dfs(root)[0]` — the LCA node.

### Why This Approach?

This is the same approach as Problem 74 (Smallest Subtree with all the Deepest Nodes), since both problems are functionally identical — finding the LCA of the deepest leaves is equivalent to finding the smallest subtree containing all deepest nodes:
- **Time Complexity:** O(n) — Each node is visited exactly once
- **Space Complexity:** O(h) — Recursion stack depth, where h is the tree height

The depth comparison at each node elegantly determines whether the deepest leaves are concentrated on one side or split across both. When split, the current node is the lowest point that still encompasses all of them.

---
