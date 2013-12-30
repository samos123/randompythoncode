

def mergesort(x):
    n = len(x)
    if n < 2:
        return x

    mid = int(n / 2)
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []

    for k in range(0, len(left) + len(right)):
        if i == len(left):
            result.extend(right[j:])
            j += len(right[j:])
        elif j == len(right):
            result.extend(left[i:])
            i += len(left[i:])
        elif left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


print "result: ", mergesort([1, 5, 2, 4])
