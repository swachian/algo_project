class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
        
def merge_overlapping_intervals(intervals):
    Interval.__lt__ = lambda x, y : x.start <= y.start if x.start != y.start else x.end <= y.end
    
    if not intervals:
        return []

    intervals.sort()

    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if res[-1].end >= intervals[i].start:
            res[-1].end = max(res[-1].end, intervals[i].end)
        else:
            res.append(intervals[i])
    
    return res

    

    
def identify_all_interval_overlaps(intervals1, intervals2):
    m = len(intervals1)
    n = len(intervals2)
    
    res = []
    i, j = 0, 0
    while i < m and j < n:
        
        L1 = intervals1[i]
        L2 = intervals2[j]
        if L1.start > L2.start:
            L1, L2 = L2, L1
        if L1.end >= L2.start:
            res.append(Interval(max(L1.start, L2.start), min(L1.end, L2.end)))

        if intervals1[i].end >= intervals2[j].end:
            j += 1
        else: 
            i += 1
            
    return res

def largest_overlap_of_intervals(intervals):
    Start = 'S'
    End = 'E'
    points_inf = []
    for interval in intervals:
        points_inf.append((interval.start, Start))
        points_inf.append((interval.end, End))
        
    points_inf.sort(key = lambda x: [x[0], x[1]])
    max_over_lap = 0
    over_lap = 0
    for point, pos in points_inf:
        if pos == End:
            over_lap -= 1
        else:
            over_lap += 1
            max_over_lap = max(max_over_lap, over_lap)
        
    return max_over_lap