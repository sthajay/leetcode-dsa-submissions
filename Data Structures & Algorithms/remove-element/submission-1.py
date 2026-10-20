class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Brute Force Solution
        # ans = []
        # for n in nums:
        #     if n != val:
        #         ans.append(n)
        
        # for i in range(len(ans)):
        #     nums[i] = ans[i]
        
        # return len(ans)

        # Time Complexity = O(n)
        # Space Complexity = O(n)

        # Optimal Solution
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1
        
        # return k
        # Too much copying elements even if not necessary
        # Time Complexity = O(n)
        # Space Complexity = O(1)

        # Most Optimal Solution
        i = 0
        n = len(nums)
        while i < n :
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else: 
                i += 1
        
        return n
        # Time Complexity = O(n)
        # Space Complexity = O(1)














    

        
        