class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        heap = []

        for num in nums:
            freq[num]+=1

        
        for key,v in freq.items():
            heapq.heappush(heap, (-v,key))

        ans = []
        while heap and k>0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        
        return ans