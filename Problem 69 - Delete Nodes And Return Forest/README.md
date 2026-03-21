# 1110. Delete Nodes And Return Forest

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/delete-nodes-and-return-forest/description/)

---

## Problem Description

Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

---

## Examples

**Example 1:**

![Delete Nodes And Return Forest Example 1](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)

```
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]  
Output: [[1,2,null,4],[6],[7]]  
Explanation: Deleting nodes 3 and 5 splits the tree into three separate trees
rooted at 1, 6, and 7.
```

**Example 2:**

```
Input: root = [1,2,4,null,3], to_delete = [3]  
Output: [[1,2,4]]  
Explanation: Deleting node 3 leaves the rest of the tree intact as a single tree.
```

---

## Constraints

- The number of nodes in the given tree is at most `1000`.  
- Each node has a distinct value between `1` and `1000`.  
- `to_delete.length <= 1000`  
- `to_delete` contains distinct values between `1` and `1000`.

---

## Solution Strategy

To solve this problem, I used a **post-order DFS with deletion** approach:

1. **Convert** `to_delete` into a set for O(1) lookups
2. **Initialize** an empty list `forest` to collect root nodes of remaining trees
3. **Define a recursive `dfs(node)`**:
   - If `node` is `None`, return `None`
   - **Recurse** on left and right children first (post-order), reassigning `node.left` and `node.right` to the return values
   - **If the node should be deleted**: add its non-null children to `forest` (they become new tree roots) and return `None` to detach it from its parent
   - **Otherwise**: return the node as-is
4. **Run** `dfs(root)` — if the root itself survives, add it to `forest`
5. **Return** `forest`.

### Why This Approach?

Post-order traversal ensures children are processed before their parent:
- **Time Complexity:** O(n) — Each node is visited exactly once
- **Space Complexity:** O(n) — The deletion set stores up to `to_delete.length` values, plus O(h) recursion stack

By processing bottom-up, when a node is deleted, its children have already been resolved. The children of a deleted node naturally become new tree roots, and returning `None` cleanly severs the deleted node from its parent.

---
