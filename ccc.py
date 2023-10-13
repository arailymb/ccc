#task 1
n = int(input("Enter any number : "))
i = 2 
while i <= n:
    print(i)
    i += 2


#task 2
n = int(input("Enter a positive integer N: "))

factorial = 1
while n > 1:
    factorial = factorial * n
    n = n - 1

print(factorial)


#task 3
while True:
    n= int(input("Enter a number: "))
    if n == 42:
        print("Number 42 is entered. Terminating the program!")
        break


#task 4
str = input("Enter string: ")

count_a = 0

for char in str:
    if char == 'a':
        count_a += 1

print(count_a)


#task 5
n = input("Please enter a number: ")

sum_of_digits = 0

for char in n:
    sum_of_digits += int(char)

print(sum_of_digits)


#task 6
n = int(input("Please enter a positive integer: "))

a, b = 0, 1
count = 0

print("The first", n, "Fibonacci numbers are:")

while count < n:
    print(a, end=" ")
    
    next_fib = a + b
    
    a, b = b, next_fib

    count += 1


#task 7
string = input("Enter a string: ")
reversed_string = string[::-1]  
print("Reversed string:", reversed_string)


#task 8
sum_of_odds = 0

while True:
    num = input("Enter a number (or 'stop' to quit): ")
    
    if num == 'stop':
        break

    num = int(num)
    
    if num % 2 == 0:  
        continue  
    
    sum_of_odds += num

print("Sum of odd numbers:", sum_of_odds)


#task 9 
import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too small.")
    else:
        print("Too large.")


#task 10
string = input("Enter a string: ")
reversed_string = string[::-1]

if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#task 11
x = float(input("Enter a number (X): "))
y = int(input("Enter the power (Y): "))

result = 1
count = 0

while count < y:
    result *= x
    count += 1

print(f"{x} to the power of {y} is: {result}")


#task 12
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a positive integer (N): "))

number = 2

while number <= n:
    if is_prime(number):
        print(number, end=" ")
    number += 1


#task 13
number = input("Enter a number: ")
reversed_number = number[::-1]
print("Reversed number:", reversed_number)


#task 14
def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

number = int(input("Enter a number: "))

while not is_prime(number):
    number = next_prime(number)
    print(f"The next prime number is {number}")
    continue
print(f"{number} is prime!")

#task 15 
def caesar_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

string = input("Enter a string: ")
n = int(input("Enter the shift (N): "))
encrypted_string = caesar_cipher(string, n)
print("Encrypted string:", encrypted_string)
