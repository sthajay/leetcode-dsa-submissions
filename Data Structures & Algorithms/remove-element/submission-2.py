class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Optimal Solution
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        
        return n
        # TC = O(n)
        # SC = O(1)
        # where n = length of nums


        # Brute Force Solution - I
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        # TC = O(n)
        # SC = O(1)
        # where n = length of nums
        # Too many replacements


        # Brute Force Solution - I
        ans = []
        for n in nums:
            if n != val:
                ans.append(n)
        
        for i, n in enumerate(ans):
            nums[i] = n
        
        return len(ans)
        # TC = O(n)
        # SC = O(n)
        # where n = length of nums





    

        
        