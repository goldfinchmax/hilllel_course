x = int(input("введи число 1: \n "))
diya = input("введи дію (+, -, *, /), яку потрібно виконати між 2-ма числами x та y: \n ")
y = int(input("введи число 2: \n "))

if diya == '+':
    z = x + y
    print(z)
elif diya == '-':
    z = x - y
    print(z)
elif diya == '*':
    z = x * y
    print(z)
elif diya == '/' and y != 0:
    z = x / y
    print(z)
elif diya not in ['+', '-', '*', '/']:
    print("Операція не підтримується, введи іншу операцію, одну з вказаних (+, -, *, /)")
else:
    print("Введи інше число, на 0 ділити не можна")