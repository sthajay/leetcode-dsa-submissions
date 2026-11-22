class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Optimal Solution  - Minheap
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
        # TC = O(n log k)
        # Each push/pop takes O(log k), repeated n times.
        # SC = O(k) for the minHeap.
        # where n = length of nums, k = kth largest position


        # Brute Force - Minheap
        # heapq.heappush(minHeap, num) automatically maintains the min-heap property.
        # heapq.heappop(minHeap) also maintains the heap property.
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]

        # TC = O(n) + O((n-k) log n) = O(n + (n-k) log n)
        # heapify takes O(n), and popping (n-k) times takes O((n-k) log n).
        # SC = O(1) auxiliary space (heapify modifies nums in place).
        # where n = length of nums, k = kth largest position


        # Brute Force Solution
        nums.sort()
        for i in range(len(nums) - 1, -1 , - 1):
            k -= 1
            if k == 0:
                return nums[i]

        # TC = O(n log n) + O(k) = O(n log n)
        # Sorting takes O(n log n), and the loop runs k times (worst case k = n).
        # SC = O(n) worst case due to Python's Timsort.
        # where n = length of nums, k = kth largest element to find