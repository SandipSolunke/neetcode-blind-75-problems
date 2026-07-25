class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for i in range(len(nums)):
            freq[nums[i]]+=1



        heap = []
        for key,val in freq.items():
            heapq.heappush(heap, (-val,key))
        ans = []
        while k>0 and heap:     
            ans.append(heapq.heappop(heap)[1])
            k-=1

        return ans
            