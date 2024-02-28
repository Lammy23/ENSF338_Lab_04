# ## Complexity Analysis

def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

# The worst case complexity is O(n^2). 
# This would require all the elements in `li` to be greater than 5 as the 
# second `for` loop will always run.

# The best case complexity is O(n). 
# This case would require all the elements in `li` to be less 
# than 5 as the second `for` loop will never run.

# The average case complexiy is O(n^2). 
# This case could occur if all the elements in `li` were random so that about half
# the data is less than 5 and the other half greater.In this case, the 
# second for loop will run about half the time.

# The average, best and worst case are not the same. 
# However, we can easily modify the code to fit this requirement by removing
# the if statement.

def processdata(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2

