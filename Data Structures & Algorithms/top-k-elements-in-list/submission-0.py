class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for i in nums:
            if i in vals:
                vals[i] += 1
            else:
                vals[i] = 0
        return sorted(vals, key=vals.get, reverse = True)[:k]