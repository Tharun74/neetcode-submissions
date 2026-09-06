class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for ele in nums:
            freq[ele] = freq.get(ele, 0) + 1
        
        for key, value in freq.items():
            bucket[value].append(key)
        
        k_count = 0

        for i in range(len(bucket) - 1, -1, -1):
            if k_count != k:
                for ele in bucket[i]:
                    result.append(ele)
                    k_count += 1
        
        return result


        



