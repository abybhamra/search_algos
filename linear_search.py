array = [4, 2, 0, 19, 6, 44]

num = 0

for i in range(len(array)):
    if array[i] == num:
        print("number [%s] found at [%s] position in the array." % (num, i))
        break
