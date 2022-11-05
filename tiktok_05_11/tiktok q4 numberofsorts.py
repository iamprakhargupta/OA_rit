


def exchace(arr):
    ans = 0
    N=len(arr)
    temp = arr.copy()
    temp.sort()
    for i in range(N):

        if (arr[i] != temp[i]):
            ans += 1

            swap(arr, i,
                 indexOf(arr, temp[i]))
            # temp = arr[i]
            # arr[i] = arr[indexOf(arr, temp[i])]
            # arr[indexOf(arr, temp[i])] = temp

    return ans


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def indexOf(arr, ele):
    for i in range(len(arr)):
        if (arr[i] == ele):
            return i
    return -1


print(exchace([3,1,2,5,4]))