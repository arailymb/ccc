#task 1
n = int(input("Enter a positive integer N: "))

i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


#task 2
n = int(input("Enter a positive integer N: "))

factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"Factorial of {n} is {factorial}")


#task 3
while True:
    number = int(input("Enter a number: "))
    if number == 42:
        print("Number 42 is entered. Terminating the program!")
        break
