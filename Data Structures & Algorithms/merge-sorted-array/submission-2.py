class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Optimal Solution - Three Pointers
        last = m + n - 1
        # m and n = length of arrays so we must do m - 1 and n - 1 for getting index
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # Cleaning up nums2 if any numbers exist
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        # Time Complexity = O(m + n)
        # Space Complexity = O(1)
        # where m = no. of elements in nums1 and n = no. of elements in nums2
        
        # Brute Force Solution - Two Pointers

        # i = j = 0
        # res = []
  
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1
        
        # res.extend(nums1[i:m])
        # res.extend(nums2[j:n])

        # # nums1 = res   # Reassigns the local variable
        # nums1[:] = res  # Modifies the original list in-place

        # Time Complexity = O(m + n)
        # Space Complexity = O(m + n)
        # where m = no. of elements in nums1 and n = no. of elements in nums2



        