class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        # TC = O(m + n) 
        # where m = length of string s
        # n = length of string t
        # SC = O(1) since we have at most 26 different characters

        