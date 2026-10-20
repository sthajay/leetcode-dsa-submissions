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
        # Space Complexity = O(n)
        # Auxiliary Space Complexity = O(1) (excluding the output array)


        # Optimal Solution
        # n = len(nums)
        # ans = [0] * (2 * n)
        # for i in range(n):
        #     ans[i] = ans[i + n] = nums[i]
        # return ans
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        # Auxiliary Space Complexity = O(1) (excluding the output array)

        # General solution if the interview asks about concatenation for more than two time
        ans = []
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        
        return ans

        # Time Complexity = O(n) 
            # It wouldn't be O(n^2) as the 2 is constant. And, we can replace 2 with any numbers to concatenate it multiple times
        # Space Complexity = O(n)
        # Auxiliary Space Complexity = O(1) (excluding the output array)





    


















