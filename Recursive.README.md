# Recursive factorial
This calculates the factorial of the number entered by the user using direct recursion.
## How it works
Function recursive_factorial(x):
1. Carriers out the operation of getting the factorial of the number entered
2. If number(x) is 0 or 1 result will be 1 
3. Else the n * recursive_factorial(x-1) 

While True loop:
1. Asks user to input a value that is positive and if negative it asks the user to enter a value again
2. Try-except catches an error when the user does not input a number.
3. It asks the user to enter a value again