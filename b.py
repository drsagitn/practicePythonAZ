def lengthSubsequenceShoppers(inputList):
    # WRITE YOUR CODE HERE
    l = len(inputList)
    ret = []
    curr = 0
    unique_list = set(inputList)
    for letter in unique_list:
        indexs = indexInArray(letter, inputList)
        if (indexs[1] > indexs[0] and indexs[1] > curr):
            ret.append(indexs[1] - curr)
            curr = indexs[1]
    return ret


def indexInArray(letter, arr):
    ret = []
    for i in range(0, len(arr)):
        try:
            idx = arr.index(letter, i)
            ret.append(idx)
        except Exception:
            return [min(ret) + 1, max(ret) + 1]
    return [min(ret) + 1, max(ret) + 1]