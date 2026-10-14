class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Brute Force Solution
        # ans = []
        # for n in nums: 
        #     ans.append(n)
        
        # for n in nums:
        #     ans.append(n)
        
        # return ans

        # Time Complexity = O(n)
        # Space Complexity = O(n), including output space
        # Auxiliary Space Complexity = O(1), exluding output space

        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        
        return ans
        # Time Complexity = O(n)
        # Space Complexity = O(n), including output space
        # Auxiliary Space Complexity = O(1), exluding output space

        # i, n = 0, len(nums)
        # ans = [0] * 2 * n
        
        # while i < n:
        #     ans[i] = nums[i]
        #     ans[i + n] = nums[i]
        #     i += 1
        
        # return ans
        #  Time Complexity = O(n)
        # Space Complexity = O(n), including output space
        # Auxiliary Space Complexity = O(1), exluding output space
        