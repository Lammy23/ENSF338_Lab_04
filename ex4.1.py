def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2
    print (li)

list = [10,12,13,14,14,5]


processdata(list)

# Q 4.1) State and justify what is the best, worst and average case
#        complexity for the code in the previous slide [0.2 pts]

# A 4.1) Worst case would be a numbers in the list being 5 or over as this would require the code to run both for loops len(li) times which gives O(n^2)
#        Best case would be all numbers being below 5 and would just iterarte through the list len(li) amount of times which gives O(n)
#        Average case would be half the entries in the list would be above 5 and the other half woould be below 5 which would give O(n^2) which would be closer to worst case

# Q 4.2) Are average, best, and worst case complexity the same? If not, produce a modified version of the code above for which average,
#        best, and worst case complexity are equivalent. [0.2 pts]

# A 4.2) Worst case and Average Case are the same with O(n^2) however Best case is different with O(n). In order to have all cases be equivalent, 
#        we would need to remove the if statement so that it will always iteratte through each element and use both for loops which give all cases a O(n^2) complexiity,

# A 4.2 CODE Below:

def processdatanew(li):
    for i in range(len(li)):
            for j in range(len(li)):
                li[i] *= 2
    print (li)

processdatanew(list)