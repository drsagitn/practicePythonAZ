def main():
    # inputList = ['a', 'b', 'c', 'd', 'a', 'e', 'f', 'g', 'h', 'i', 'j', 'e']
    inputList = ['a', 'b', 'c']

    l = len(inputList)
    ret = []
    curr = 0
    unique_list = set(inputList)
    for letter in unique_list:
        indexs = indexInArray(letter, inputList)
        if (indexs[1] > indexs[0] and indexs[1] > curr):
            ret.append(indexs[1] - curr)
            curr = indexs[1]
    if len(ret) == 0:
        for i in range(l):
            ret.append(1)
    print ret
    return ret


def indexInArray(letter, arr):
    print letter
    ret = []
    for i in range(0, len(arr)):
        try:
            idx = arr.index(letter, i)
            ret.append(idx)
        except Exception:
            return [min(ret) + 1, max(ret) + 1]
    return [min(ret) + 1, max(ret) + 1]


def selectPairs(targetDuration, arr):
    ret = []
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == targetDuration):
                if (len(ret) <= 0 or
                        max(arr[i], arr[j]) > max(arr[ret[0]], arr[ret[1]])
                ):
                    ret = [i, j]
    return ret



def getPairsCount(arr, n, sum):
    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1

    twice_count = 0
    ret = []
    for i in range(0, n):
        twice_count += m[sum - arr[i]]
        if (sum - arr[i] == arr[i]):
            ret.append()
            twice_count -= 1

    return int(twice_count / 2)


main()


