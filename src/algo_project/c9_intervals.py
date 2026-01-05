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
    if len(intervals1) > len(intervals2):
        intervals1, intervals2 = intervals2, intervals1
    
    m, n = len(intervals1), len(intervals2)
    res = []
    i = j = 0
    while i < m and j < n:
        A = intervals1[i]
        B = intervals2[j]
        if A.start > B.start:
            A, B = B, A
        if A.end >= B.start:
            res.append(Interval(B.start, min(B.end, A.end)))
        if intervals1[i].end < intervals2[j].end:
            i += 1
        else: 
            j += 1
    return res


def largest_overlap_of_intervals(intervals):
    START = "S"
    END = "E"

    # intervals.sort(key = lambda interval: [interval.start, interval.end])
    measures = []
    for interval in intervals:
        measures.append((interval.start, START))
        measures.append((interval.end, END))
    measures.sort(key = lambda x: [x[0], x[1]])
    max_count = 0
    count = 0
    for pos, t in measures:
        if t == END:
            count -= 1
        else:
            count += 1
            max_count = max(max_count, count)

    return max_count

        
