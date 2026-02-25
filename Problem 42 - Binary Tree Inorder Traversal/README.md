# 94. Binary Tree Inorder Traversal

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

---

## Problem Description

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

---

## Examples

**Example 1:**

![Inorder Traversal Example 1](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

```
Input: root = [1,null,2,3]  
Output: [1,3,2]
```

**Example 2:**

![Inorder Traversal Example 2](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]  
Output: [4,2,6,5,7,1,3,9,8]
```

**Example 3:**

```
Input: root = []  
Output: []
```

**Example 4:**

```
Input: root = [1]  
Output: [1]
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.  
- `-100 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS** approach:

1. **Initialize** an empty `result` list
2. **Define a recursive `inorder(node)` function**:
   - Base case: if `node is None`, return
   - Recurse on the **left** subtree: `inorder(node.left)`
   - **Append** the current node's value: `result.append(node.val)`
   - Recurse on the **right** subtree: `inorder(node.right)`
3. **Call** `inorder(root)` and **return** `result`.

### Why This Approach?

Recursive inorder traversal naturally follows the Left → Root → Right pattern:
- **Time Complexity:** O(n) - We visit every node exactly once
- **Space Complexity:** O(n) - Result list stores n values, plus O(h) recursion stack

The inorder traversal visits the left subtree first, then processes the current node, then the right subtree. This produces a sorted output for binary search trees.

---
