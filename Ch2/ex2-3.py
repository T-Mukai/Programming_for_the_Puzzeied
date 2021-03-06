# Exercise 3: Imagine that there is a weight associated with each celebrity dependent on how much you like that particular celebrity.
# This can be represented in the schedule as a 3-tuple, e.g., (6.0, 8.0, 3).
# The start time is 6.0, end time is 8.0 and the weight is 3.
# Modify the code so you find the time that the celebrities with maximum total weight are available.

sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]

def bestTimeToPartySmartWeight(schedule):
    #Convert schedule to list of start times and end times marked as such
    times = []
    for c in schedule:
        times.append((c[0], 'start', c[2]))
        times.append((c[1], 'end', c[2]))

    #Sort the list of times.
    #Each time is a start or end time of a celebrity sighting.
    sortlist(times)
##    print times

    maxweight, time = chooseTime(times)


    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxweight, 'celebrities will be attending!')


#Sort the elements of tlist in ascending order
#Sorting is based on the value of the first item of the element tuple
def sortlist(tlist):
    for index in range(len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            #Sort based on first item of tuple
            if tlist[ismall][0] > tlist[i][0]:
                ismall = i
        #Swap the positions of the elements at index and ismall indices
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]

    return


def chooseTime(times):

    rweight = 0
    maxweight = 0
    time = 0

    #Range through the times computing a running count of celebrities
    for t in times:
        if t[1] == 'start':
            rweight = rweight + t[2]
        elif t[1] == 'end':
            rweight = rweight - t[2]
        if rweight > maxweight:
            maxweight = rweight
            time = t[0]

    return maxweight, time


bestTimeToPartySmartWeight(sched3)
