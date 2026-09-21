class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        ma = 0
        while i < j:
            h = min(heights[i], heights[j])
            w = j - i
            a = h * w
            ma = max(a, ma)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return ma 
        