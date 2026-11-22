class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Theres no maxHeap in python so we simulate maxHeap using minHeap
        stones = [-s for s in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # it should be first > second, but we set all values as negative 
            # so thats why we are doing this
            if second > first:
                heapq.heappush(stones, first - second)
            
        
        return abs(stones[0]) if stones else 0




        