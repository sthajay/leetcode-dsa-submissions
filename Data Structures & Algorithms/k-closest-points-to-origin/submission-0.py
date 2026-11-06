class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            # dist is first so the heap is ordered by distance
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res

        # TC = O(n) + O(n) + O(k log n) 
        # = O(n + k log n)
       
        # Space Complexity = O(n)
        #  n = total number of points in points
        # k = number of closest points you need to return
        
        