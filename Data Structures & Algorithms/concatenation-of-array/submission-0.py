class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for ele in nums:
            ans.append(ele)
        
        return ans
        