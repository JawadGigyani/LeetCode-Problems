# 508. Most Frequent Subtree Sum

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/most-frequent-subtree-sum/description/)

---

## Problem Description

Given the `root` of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The **subtree sum** of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

---

## Examples

**Example 1:**

![Most Frequent Subtree Sum Example 1](https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg)

```
Input: root = [5,2,-3]  
Output: [2,-3,4]  
Explanation:
Subtree sum of node 2: 2
Subtree sum of node -3: -3
Subtree sum of node 5: 5 + 2 + (-3) = 4
Each subtree sum occurs once, so all are returned.
```

**Example 2:**

![Most Frequent Subtree Sum Example 2](https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg)

```
Input: root = [5,2,-5]  
Output: [2]  
Explanation:
Subtree sum of node 2: 2
Subtree sum of node -5: -5
Subtree sum of node 5: 5 + 2 + (-5) = 2
The sum 2 appears twice (most frequent), so only [2] is returned.
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10⁴]`.  
- `-10⁵ <= Node.val <= 10⁵`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS with frequency counting** approach:

1. **Initialize** a `defaultdict(int)` called `freq` to track subtree sum frequencies
2. **Define a recursive `dfs(node)`**:
   - If `node` is `None`, return `0`
   - **Recurse** on left and right subtrees to get their sums
   - **Compute** the subtree sum `s = node.val + left + right`
   - **Record** the sum by incrementing `freq[s]`
   - **Return** `s` to the parent call
3. **Run** `dfs(root)` to populate all subtree sums
4. **Find** `max_freq` — the highest frequency among all sums
5. **Collect** all sums whose frequency equals `max_freq` and return them.

### Why This Approach?

Post-order DFS naturally computes subtree sums bottom-up:
- **Time Complexity:** O(n) — Each node is visited exactly once
- **Space Complexity:** O(n) — Frequency map stores at most n sums, plus O(h) recursion stack

By computing sums bottom-up, each node's subtree sum is built from its children's already-computed sums. The frequency map then makes finding the most common sum(s) a simple linear scan.

---
