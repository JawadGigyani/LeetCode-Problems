import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        answer = [""] * n

        max_heap = [(-s, i) for i, s in enumerate(score)]

        heapq.heapify(max_heap)

        rank = 1
        while max_heap:
            _, org_index = heapq.heappop(max_heap)

            if rank == 1:
                answer[org_index] = "Gold Medal"
            elif rank == 2:
                answer[org_index] = "Silver Medal"
            elif rank == 3:
                answer[org_index] = "Bronze Medal"
            else:
                answer[org_index] = str(rank)
            
            rank += 1
        
        return answer