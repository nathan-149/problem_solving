class Solution:
    def merge(self, intervals):
        if not intervals: 
            return []
        intervals = sorted(intervals, key= lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]

        result = []
        for [first,second] in intervals:
            if(first >= start and first <= end):
                end = max(end, second)
            else:
                result.append([start, end])
                start = first
                end = second
        result.append([start,end])
        return result

sol = Solution()

x = sol.merge([[1,4],[4,5]])

print(x)
