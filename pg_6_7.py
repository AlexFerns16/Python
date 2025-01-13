# a number is said to be a prime number if the number
# is divisible by itself and
# if the number is not divisible by it's multiples

num = int(input('Enter an integer: '))
i=2

# 'num' is a didvident
# 'i' is a divisor
# here 'num-1' is considered because if 'num=5' and when 'i' increments to '5', 
# then 'num % i' would result in '0' as remainder. since the number is divisible by itself. 
# which would result in wrong output as 'not a prime number' since the number is 'not divisible by it's multiples'.

while i <= num-1:     # or while i < num:               
  if num % i == 0:
    print(num, 'is not a prime number')
    break
  i += 1
else:

  # the else block goes to work when the while loop is not stopped abruptly
  # meaning when the while condition turns to 'False' the else block is executed
  # if the 'break' statement is executed then the else block of the while loop does not go to work

  print(num, 'is a prime number')
