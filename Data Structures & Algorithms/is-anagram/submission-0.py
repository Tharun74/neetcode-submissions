class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        scount = {}
        tcount = {}
        
        for c in s:
            if c not in scount:
                scount[c] = 1
            else:
                scount[c] += 1

        for c in t:
            if c not in tcount:
                tcount[c] = 1
            else:
                tcount[c] += 1
        
        return scount == tcount
            
        