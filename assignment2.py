#Task 1: Check if a Number is Even or Odd

num=int(input('enter the number : '))

if num % 2 == 0:
  print(f'{num} is even number')
else:
  print(f'{num} is odd number')





#Task 2: Sum of Integers from 1 to 50 Using a Loop

a=0
for i in range(1,51):
  a+=i
print('the sum of number is:',a)