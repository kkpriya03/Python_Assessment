"""
1. Print numbers from 1 to 10 using a while loop.

n = 1
while n <= 10:
    print(n)
    n=n+1

2. Print even numbers from 1 to 20.
n = 1
while n <= 20:
    if n%2==0:
        print(n)
    n=n+1

3. Print odd numbers from 1 to 20.
    
n = 1
while n <= 20:
    if n%2!=0:
        print(n)
    n=n+1

4. Print numbers from 10 to 1 (reverse order).
n = 10
while n >= 1:
    print(n)
    n=n-1
    
5. Print multiplication table of 5 using while loop.
i = 1
while i <= 10:
    print(5 * i)
    i=i+1

6. Find the sum of first 10 natural numbers using while loop.
n = 1
sum = 0
while n <= 10:
    sum=sum+n
    n=n+1
print("Sum =", sum)

7. Find factorial of a number entered by user.

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact=fact*i
    i=i+1
print("Factorial =", fact)

8. Count number of digits in a given number.

n=int(input("Enter the number:"))
count=0
while(n>0):
    r=n%10
    count=count+r
    n=n//10
print("Digit count is:",count)

9. Reverse a number using while loop.
n=int(input("Enter the number:"))
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverese is:",rev)

10. Check whether a number is palindrome or not using while loop.

n=int(input("Enter the number:"))
pal=0
while(n>0):
    r=n%10
    pal=pal*10+r
    n=n//10
print("palindrome number is:",pal)

Part 3 – Pattern Based
11. Print pattern:
*
**
***
****
*****
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()

12. Print pattern:
1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

13. Ask user to enter password until correct password is entered.

correct_password = "1234"

while True:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong password, try again")
14. Create a number guessing game:
• Generate a random number (1–10)
• Keep asking user until they guess correctly

   import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))
    
    if guess == number:
        print("Correct! You guessed it 🎉")
        break
    else:
        print("Wrong guess, try again")

15. Keep taking input numbers until user enters 0, then print total sum.
add=0
while True:
    num=int(input("Enter the number(0 for Exit):"))
    add=add+num
    if num==0:
        break
    print("Total:",add)

16. Print Fibonacci series up to N terms using while loop.
n = int(input("Enter number of terms: "))
a = 0
b = 1
count = 0
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count=count+1

17. Check whether a number is Armstrong number.
    
num=int(input("Enter the number:"))
copy=num
add=0
while num>0:
    rem=num%10
    add=add+rem**3
    num=num//10
if copy==add:
    print("Armstrong")
else:
    print("Not Armstrong")

18. Print prime numbers between 1 to 50 using while loop.
print("All prime number are:")
n = 2
i = 1
count = 0
while n <= 50:
    if i <= n:
        if n % i == 0:
            count=count+1
        i=i+1
    else:
        if count == 2:
            print(n, end=" ")
        n=n+1
        i=1
        count = 0

"""







