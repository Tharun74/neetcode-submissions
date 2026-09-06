class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = [0] * 26
            for ch in word:
                pos = ord(ch) - ord('a')
                key[pos] += 1
            key = tuple(key)
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())
      
            
        

        