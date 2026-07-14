def countSort(a):
    n = len(a)
    max_ = max(a)+1
    res = [0 for i in range(n)]
    counts = [0 for i in range(max_)]
    b = [0] * len(counts)
    b[0] = counts[0]
    for i in a:
        counts[i] += 1
    for i in range(len(counts)):
        b[i] = counts[i] + b[i-1]
    for i in a[::-1]:
        res[b[i]-1] = i
        b[i] -= 1
    print(res)
countSort([0,1,5,5,4,3,4,4,2,3,0,1,2])