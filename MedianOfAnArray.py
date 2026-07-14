def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        median = arr[n // 2]
    return median
arr = [7, 2, 5, 1, 9]
print("Median:", find_median(arr))
