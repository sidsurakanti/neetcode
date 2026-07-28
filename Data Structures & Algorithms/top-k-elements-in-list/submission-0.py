class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for n in nums:
            if n not in d.keys():
                d[n] = 0
            d[n] += 1
        
        return [k for k,v in sorted(d.items(), key=lambda i: i[1], reverse=1)][:k]
