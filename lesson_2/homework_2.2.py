number = int(input("Введіть 5-ти значне ціле число: \n "))
five = number // 10000
four = (number % 10000) // 1000
three = (number % 1000) // 100
two = (number % 100) // 10
one = (number % 10) // 1

print(one)
print(two)
print(three)
print(four)
print(five)