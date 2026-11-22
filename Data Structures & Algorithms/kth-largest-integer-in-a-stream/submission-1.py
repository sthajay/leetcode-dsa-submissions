class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

    # TC:
    # __init__ = O(n + (n-k) * log n) if n > k, otherwise O(n)
    # add() = O(log k)
    #
    # SC = O(k) for the maintained heap
    #
    # n = number of initial elements
    # k = kth largest element to maintain
        
        
