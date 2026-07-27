class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        ans = -1
        for num in nums:
            heapq.heappush(heap, -num)
        
        while k>0:
            if len(heap)<=0:
                return -1
            ans = heapq.heappop(heap)
            k-=1
        
        return -ans