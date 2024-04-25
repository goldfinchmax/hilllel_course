lst = [1, 2, 3, 4, 5]
#lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
#lst = []
#lst = [1]
print(lst)

size = len(lst)
halfsize = int(size / 2)

if size % 2 == 0:
    index1 = halfsize
else:
    index1 = halfsize + 1

sublist1 = lst[:index1]

sublist2 = lst[index1:]

newlist = [sublist1] + [sublist2]

print(newlist)