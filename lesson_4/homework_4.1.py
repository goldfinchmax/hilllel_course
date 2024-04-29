lst = [0, 1, 0, 12, 3]
lst = [0]
lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
zeros = lst.count(0)
lst = [x for x in lst if x != 0]
lst.extend([0] * zeros)
print(lst)