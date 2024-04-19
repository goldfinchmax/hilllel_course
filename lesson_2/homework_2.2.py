number = int(input("Введіть 5-ти значне ціле число: \n "))
five = number // 10000
four = (number % 10000) // 1000
three = (number % 1000) // 100
two = (number % 100) // 10
one = (number % 10) // 1

result = (one*10000 + two*1000 + three*100 + four*10 + five*1)
print(result)