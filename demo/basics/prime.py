# Accept a number and display whether it is prime

num = int(input("Enter a number :"))

prime_number = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        prime_number = False
        break

if prime_number:
    print("Prime Number")
else:
    print("Not a prime number")
