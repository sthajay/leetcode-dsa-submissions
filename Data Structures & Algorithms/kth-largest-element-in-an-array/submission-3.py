class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Most Optimal Solution - Quick Select (Quick Sort but only for half)

        k = len(nums) - k
        l, r = 0, len(nums) - 1
        while l <= r: 
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                
            nums[p], nums[r] = nums[r], nums[p]
        
            if p > k:
                r = p - 1
            elif p < k:
                l = p + 1
            else:
                return nums[p]
            
        # TC = O(n) average, O(n^2) worst case
        #      Each partition takes O(n), and we search only one side.
        #      Worst case occurs with repeatedly unbalanced partitions.
        # SC = O(1) auxiliary space (in-place, no recursion).
        # Output SC = O(1), returning one integer.
        # where n = length of nums, k = kth largest position

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