class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = j = 0
        res = []
  
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        res.extend(nums1[i:m])
        res.extend(nums2[j:n])

        # nums1 = res   # Reassigns the local variable
        nums1[:] = res  # Modifies the original list in-place

        # Time Complexity = O(m + n)
        # Space Complexity = O(m + n)
        # where m = no. of elements in nums1 and n = no. of elements in nums2



        