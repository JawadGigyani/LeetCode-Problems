# 865. Smallest Subtree with all the Deepest Nodes

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/)

---

## Problem Description

Given the `root` of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the **deepest** if it has the largest depth possible among any node in the entire tree.

The **subtree** of a node is a tree consisting of that node, plus the set of all descendants of that node.

---

## Examples

**Example 1:**

![Smallest Subtree Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]  
Output: [2,7,4]  
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but
node 2 is the smallest subtree among them, so we return it.
```

**Example 2:**

```
Input: root = [1]  
Output: [1]  
Explanation: The root is the deepest node in the tree.
```

**Example 3:**

```
Input: root = [0,1,3,null,2]  
Output: [2]  
Explanation: The deepest node in the tree is 2, the valid subtrees are the
subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
```

---

## Constraints

- The number of nodes in the tree will be in the range `[1, 500]`.  
- `0 <= Node.val <= 500`  
- The values of the nodes in the tree are unique.

---

## Solution Strategy

To solve this problem, I used a **post-order DFS returning (node, depth) pairs** approach:

1. **Define a recursive `dfs(node)`** that returns a tuple `(subtree_root, depth)`:
   - If `node` is `None`, return `(None, 0)`
   - **Recurse** on left and right children to get `(left_node, left_depth)` and `(right_node, right_depth)`
   - **If `left_depth > right_depth`**: The deepest nodes are all on the left side — return `(left_node, left_depth + 1)`
   - **If `right_depth > left_depth`**: The deepest nodes are all on the right side — return `(right_node, right_depth + 1)`
   - **If depths are equal**: Both sides contain deepest nodes — the current `node` is the lowest common ancestor, so return `(node, right_depth + 1)`
2. **Return** `dfs(root)[0]` — the node component of the result.

### Why This Approach?

By comparing subtree depths bottom-up, we naturally find the smallest enclosing subtree:
- **Time Complexity:** O(n) — Each node is visited exactly once
- **Space Complexity:** O(h) — Recursion stack depth, where h is the tree height

The key insight is that if both subtrees have equal max depth, the current node must be the answer since deepest nodes exist on both sides. If one side is deeper, the answer lies entirely within that side. This elegantly narrows down to the smallest subtree in a single pass.

---
