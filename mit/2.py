def findPeakUtil(arr, low, high, n): 
    mid = low + (high - low)/2 
    mid = int(mid)
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n) 
    else:
        return findPeakUtil(arr, (mid + 1), high, n) 
  
  
def findPeak(arr, n): 
    return findPeakUtil(arr, 0, n - 1, n) 
  
  
arr = [1, 3, 20, 4, 1, 0] 
n = len(arr) 
print("Index of a peak point is", findPeak(arr, n)) 
