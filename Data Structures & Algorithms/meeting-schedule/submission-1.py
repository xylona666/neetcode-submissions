"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        cur=0
        for i  in  intervals:
            if  i.start>=cur:
                cur = i.end
                print(cur)
            else:
                return False
        return True