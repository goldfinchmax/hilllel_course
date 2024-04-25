#lst = [12, 3, 4, 10]
#lst = [1]
#lst = []
lst = [12, 3, 4, 10, 8]
#lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(lst)
if not lst :
    x = lst
else:
    x = lst.pop()
    lst.insert(0, x)
print(lst)
