"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = sorted(intervals)
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 0:
            return 0

        heap = []
        heapq.heappush(heap,intervals[0].end)
        
        parallel_meetings = 1
        for i in range(1,len(intervals)):
            # print("i :",i)
            # print(heap)
            # print("\n")
            while len(heap)>0 and heap[0] <= intervals[i].start:
               heapq.heappop(heap)
            heapq.heappush(heap,intervals[i].end)
            parallel_meetings = max(parallel_meetings, len(heap))
        return parallel_meetings
