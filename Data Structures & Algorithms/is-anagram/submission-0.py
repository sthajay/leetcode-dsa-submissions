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

        
        print(objS)
        print(objT)
        return objS == objT

        