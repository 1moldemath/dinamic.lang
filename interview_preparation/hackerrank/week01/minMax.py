def miniMaxSum(arr):
    minSum, maxSum = 1000000000000, 0

    for i in range(len(arr)):
        copy = arr[:]
        del copy[i]
        validator = sum(copy)
        
        if validator < minSum:
            minSum = validator
            
        if validator > maxSum:
            maxSum = validator

    return minSum, maxSum