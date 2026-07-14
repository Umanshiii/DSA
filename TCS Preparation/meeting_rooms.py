'''
The goal is to find the minimum number of conference 
rooms required to accommodate a schedule of meetings, 
where each meeting has a start time and an end time 
(e.g., [[0, 30], [5, 10], [15, 20]]).

Essentially, we need to find the maximum number of
overlapping meetings at any single point in time.
'''
# intervals = [[0, 30], [5, 10], [15, 20]]

def rooms(time):
    currooms = 0
    maxrooms = 0
    start=[]
    end=[]
    for i in time:
        start.append((i[0], True))
        end.append((i[1], False))
    events=start+end
    events.sort(key=lambda x: (x[0], x[1]))
    for i in events:
        if i[1]:
            currooms+=1
        else:
            currooms-=1    
        maxrooms=max(currooms, maxrooms)

    return maxrooms