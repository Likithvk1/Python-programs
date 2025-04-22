

#Write a python program to find factorial of given number

number = int(input("Enter a number = "))

factorial = 1

for i in range(1,number+1):
    factorial = factorial * i

print(f'Factorial of {number} = {factorial}')