import heapq
def runningMedian(a):
    l = [] 
    r = [] 
    ans = []
    for x in a:
        if not l or x <= -l[0]:
            heapq.heappush(l, -x)
        else:
            heapq.heappush(r, x)

        if len(l) > len(r) + 1:
            heapq.heappush(r, -heapq.heappop(l))
        if len(r) > len(l):
            heapq.heappush(l, -heapq.heappop(r))

        if len(l) == len(r):
            m = (-l[0] + r[0]) / 2
        else:
            m = -l[0]
        ans.append(m)
    return ans
    
runningMedian([10,1,2,3,4,5,6,7,8,9,10])