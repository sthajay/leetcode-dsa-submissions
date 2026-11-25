class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimal - Single Loop
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

        # TC = O(n) 
        # where n = length of either string
        # n = length of string t
        # SC = O(1) since we have at most 26 different characters



        # Optimal - Two Separate Loops
        if len(s) != len(t):
            return False
        
        objS = {}
        objT = {}
        for i in range(len(s)):
            if s[i] not in objS:
                objS[s[i]] = 1
            
            else:
                objS[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in objT:
                objT[t[i]] = 1
                
            else:
                objT[t[i]] += 1

        return objS == objT
        # TC = O(m + n)  = O (n + n) = O(2n) = O(n) 
        # because m = n as we have already checked the length earlier
        # so, m = n = length of either string
        # n = length of string t
        # SC = O(1) since we have at most 26 different characters

        