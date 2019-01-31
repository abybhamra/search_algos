array = [4, 2, 0, 19, 6, 44]
num = 0

"""
binary search works only on sorted arrays
"""
array.sort()
print(array)

low = 0
high = len(array) - 1

while low <= high:
    mid = high + low // 2
    if array[mid] == num:
        print("number [%s] found in the array." % num)
        break
    elif num < array[mid]:
        high = mid - 1
    else:
        low = mid + 1
