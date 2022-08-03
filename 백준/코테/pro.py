def maxPosPrefixes(arr):
    arr.sort(reverse=True)

    ncheck = 0
    pcheck = 0
    if len(arr) == 1:
        if arr[0] >= 0:
            return 1
        else:
            return 0
        
    for i in range(len(arr)):
        if arr[i] < 0:
            ncheck = i
            break    
        if i == len(arr) - 1:
            return len(arr)
            
    pos = sum(arr[:ncheck])
    neg = sum(arr[ncheck:])

    if pos == 0:
        return 0
    
    tmp = 0
    for a in arr[ncheck:]:
        tmp += a
        if pos + tmp <= 0:
            return (arr.index(a))
    
    return (len(arr))


def getBingoNumber(mat, arr):
    row_list = [0] * mat_rows
    col_list = [0] * mat_columns
    for a in arr:
        for i in range(mat_rows):
            for j in range(mat_columns):
                if a == mat[i][j]:
                    row_list[i] += 1
                    col_list[j] += 1
                    if row_list[i] == mat_columns or col_list[j] == mat_rows:
                        return mat[i][j]


def getMostVisited(n, sprints):
    arr = [0] * n
    for i in range(len(sprints) - 1):
        if sprints[i] < sprints[i + 1]:
            for j in range(sprints[i] - 1, sprints[i + 1]):
                arr[j] += 1
        else:
            for j in range(sprints[i + 1] - 1, sprints[i]):
                arr[j] += 1
    return arr.index(max(arr)) + 1


def getMinimumOperations(arr):
    result = 0
    
    i, j = 0, arr_count - 1
    
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        
        elif arr[i] > arr[j]:
            j -= 1
            arr[j] += arr[j + 1]
            result += 1
        
        else:
            i += 1
            arr[i] += arr[i - 1]
            result += 1
    
    return result


def getMostVisited(n, sprints):
    arr = [0] * (n + 2)
    for i in range(len(sprints) - 1):
        if sprints[i] > sprints[i + 1]:
            start, end = sprints[i + 1], sprints[i]
        else:
            start, end = sprints[i], sprints[i + 1]

        arr[start] += 1
        arr[end + 1] -= 1
    
    result = 0
    tmp = 0
    check = -1
    for i in range(1, n + 1):
        arr[i] += tmp
        tmp = arr[i]
        if tmp > check:
            check = tmp
            result = i
    return result