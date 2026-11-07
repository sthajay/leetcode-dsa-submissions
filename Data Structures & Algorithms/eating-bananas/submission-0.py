class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
        # TC = O(n * logm)
        # SC = O(1)
        # where n = length of piles
        # m = maximum no of bananas in a pile
        
        