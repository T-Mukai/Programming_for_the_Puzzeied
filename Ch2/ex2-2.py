# Exercise 2: There is an alternative way of computing the best time to party that does not depend on the granularity of time.
# We choose each celebrity interval in turn, and determine how many other celebrity intervals contain the chosen celebrity’s start time.
# We pick the time to attend the party to be the start time of the celebrity whose start time is contained in the maximum number of other celebrity intervals.
# Code this algorithm and verify that it produces the same answer as the algorithm based on sorting.

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

def bestTimeToPartyAnotherWay(schedule):
    maxcount = 0
    time = 0

    #choose each celebrity
    for i in range(len(schedule) - 1):
        #First, count myself
        rcount = 1
        start = schedule[i][0]
        for j in range(len(schedule) - 1):
            #Count other celebrities who are in when the celebrity come.
            if i != j and schedule[j][0] <= start and schedule[j][1] > start:
                rcount += 1

        if rcount > maxcount:
            maxcount = rcount
            time = start

    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')

bestTimeToPartyAnotherWay(sched)
bestTimeToPartyAnotherWay(sched2)
