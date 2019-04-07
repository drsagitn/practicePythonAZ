def IDsOfSongs(rideDuration, songDurations):
    # WRITE YOUR CODE HERE
    pair = selectPairs(rideDuration - 30, songDurations)
    return pair


def selectPairs(targetDuration, arr):
    ret = []
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == targetDuration):
                if (len(ret) <= 0 or max(arr[i], arr[j]) > max(arr[ret[0]], arr[ret[1]])):
                    ret = [i, j]
    return ret
