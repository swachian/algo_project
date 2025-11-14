class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def merge_overlapping_intervals(intervals):
    sorted_intervals = list(intervals)
    sorted_intervals.sort(key = lambda interval: [interval.start, interval.end])
    result = [sorted_intervals[0]]
    for i in range(1, len(sorted_intervals)):
        cur_interval = result[-1]
        if cur_interval.end >= sorted_intervals[i].start:
            result[-1] = Interval(cur_interval.start, max(cur_interval.end, sorted_intervals[i].end))
        else:
            result.append(sorted_intervals[i])

    return result


def identify_all_interval_overlaps(intervals1, intervals2):
    i, j = 0, 0
    result = []
    
    while i < len(intervals1) and j < len(intervals2):
        A, B = intervals1[i], intervals2[j]
        if A.start > B.start:
            A, B = B, A
        if A.end >= B.start:
            result.append(Interval(B.start, min(A.end, B.end)))

        if intervals1[i].end < intervals2[j].end:
            i += 1
        else:
            j += 1
    return result

def largest_overlap_of_intervals(intervals):
    START = "S"
    END = "E"
    envoys = []
    for interval in intervals:
        envoys.append((interval.start, START))
        envoys.append((interval.end, END))
    
    envoys.sort(key = lambda x: [x[0], x[1]])
    
    counts = []

    for cur, status in envoys:
        count = counts[-1] if counts else 0
        if status == END:
            count -= 1
            counts.append(count)
        if status == START:
            count += 1
            counts.append(count)
         
    return max(counts)
























