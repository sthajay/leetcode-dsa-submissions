class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Brute Force Solution
        # tmp = []
        # for n in nums:
        #     if n != val: 
        #         tmp.append(n)
        
        # for i in range(len(tmp)):
        #     nums[i] = tmp[i]
        
        # return len(tmp)

        # Time Complexity = O(n)
        # Space Complexity = O(n)

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        '''
        # Time Complexity = O(n)
        # Space Complexity = O(1)

        However, this approach is copying unnecessarily. We can swap unwanted elements with elements from the end of the array.

        '''

        # Optimal Solution
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] == nums[n]
            else: 
                i += 1
        
        return n
        # Time Complexity = O(n)
        # Space Complexity = O(1)


    

        
        