class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupCount = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            if key in groupCount:
                groupCount[key].append(s)
            else:
                groupCount[key] = [s]
        return list(groupCount.values())