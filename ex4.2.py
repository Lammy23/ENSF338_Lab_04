import timeit


# Efficient Code

def efficientsort(arr, search_term, low, high):
    while low <= high:
        mid = low +(high-low)//2

        if arr[mid] == search_term:
            return True
        elif arr[mid] < search_term:
            low = mid+1
        elif arr[mid] > search_term:
            high = mid-1



# Ineffeicient Code
    
def inefficientsort(arr, search_term):
    n = len(arr)
    for i in range(n):
        if arr[i] == search_term:
            return True


Sortedarray = [1,2,3,4,5,6,7,8,9]

search = 8

efficientsortresult = efficientsort(Sortedarray, search,0,len(Sortedarray)-1)
inefficientsortresult = inefficientsort(Sortedarray, search)
