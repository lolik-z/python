def MaxList(arr):
    maxL = arr[0]
    for ele in arr:
        if ele > maxL:
           maxL = ele
    return maxL

def MinList(arr):
    minL = arr[0]
    for ele in arr:
        if ele < minL:
           minL = ele
    return minL

