# Function to calculate factorial of a number
def recursive_factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * recursive_factorial(x - 1)
    # asks user to input a number
while True:
    try:
        n = int(input("Enter a number:"))
        if n<0:
            print("Enter positive numbers!")
        else:
            break
    except ValueError:
        print("Try again!")
# prints the result
print(f"Factorial:", recursive_factorial(n))