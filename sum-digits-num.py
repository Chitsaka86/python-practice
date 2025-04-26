# function to get the sum of digits in a number
def sum_digits(k):
    add=0
    # converts input to string, checks if it's a digit and coverts the digits to int and adds the sum
    for digit in str(k):
        if digit.isdigit():
            add += int(digit)
    return add
# asks user to enter a number
v = input("Enter a number: ")
# prints the sum
print("the sum is:", sum_digits(v))