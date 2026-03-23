# 1971. Find if Path Exists in Graph

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

---

## Problem Description

There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [uᵢ, vᵢ]` denotes a bi-directional edge between vertex `uᵢ` and vertex `vᵢ`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise.

---

## Examples

**Example 1:**

![Find Path Example 1](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png)

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2  
Output: true  
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
```

**Example 2:**

![Find Path Example 2](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png)

```
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5  
Output: false  
Explanation: There is no path from vertex 0 to vertex 5.
```

---

## Constraints

- `1 <= n <= 2 * 10⁵`  
- `0 <= edges.length <= 2 * 10⁵`  
- `edges[i].length == 2`  
- `0 <= uᵢ, vᵢ <= n - 1`  
- `uᵢ != vᵢ`  
- `0 <= source, destination <= n - 1`  
- There are no duplicate edges.  
- There are no self edges.

---

## Solution Strategy

To solve this problem, I used a **DFS with adjacency list** approach:

1. **Build an adjacency list** using a `defaultdict(list)` — for each edge `[u, v]`, add `v` to `d[u]` and `u` to `d[v]`
2. **Initialize** a `seen` set with the `source` node to track visited vertices
3. **Define a recursive `dfs(node)`**:
   - If `node == destination`, return `True` (path found)
   - **Iterate** through each `neighbour` of `node`
   - If the neighbour hasn't been visited, mark it as seen and recurse — if the recursive call returns `True`, propagate it up
   - If no neighbour leads to the destination, return `False`
4. **Return** `dfs(source)`.

### Why This Approach?

DFS is a natural fit for reachability queries in graphs:
- **Time Complexity:** O(n + e) — Each vertex and edge is visited at most once
- **Space Complexity:** O(n + e) — Adjacency list storage plus the visited set and recursion stack

The `seen` set prevents revisiting nodes, avoiding infinite loops in cyclic graphs. DFS explores as deep as possible along each branch, and short-circuits as soon as the destination is found.

---
