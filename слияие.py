data =list(map(int, input().split()))


def merge_sort(data):
    if len(data) <= 1:
        return data
    m = len(data) // 2
    l = data[:m]
    r = data[m:]


    l_half = merge_sort(l)
    r_half = merge_sort(r)

    return merge(l_half, r_half)


def merge(left, right):
    data1 = []
    left_index = 0
    right_index = 0

    while left_index < len(left):
        data1.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        data1.append(right[right_index])
        right_index += 1

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1


    return data1
data1 = merge_sort(data)
print(data1)
