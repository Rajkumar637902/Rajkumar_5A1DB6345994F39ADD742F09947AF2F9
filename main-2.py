#1.1 implement a resource function to calculate the factorial of given number.
def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n - 1)


num = int(input("Entet the number : "))
print('The factorial of {} is {}'.format(num, factorial(num)))
