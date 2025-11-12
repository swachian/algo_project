class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def merge_overlapping_intervals(intervals):
    sorted_intervals = list(intervals)
    sorted_intervals.sort(key = lambda interval: [interval.start, interval.end])
    result = []
    cur_interval = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        if cur_interval.end >= sorted_intervals[i].start:
            cur_interval = Interval(cur_interval.start, max(cur_interval.end, sorted_intervals[i].end))
        else:
            result.append(cur_interval)
            cur_interval = sorted_intervals[i]
    result.append(cur_interval)
    return result






























