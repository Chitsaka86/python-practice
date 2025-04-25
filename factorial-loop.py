# function to calculate factorial
def factorial_use_loops(x):
    answer = 1
    for n in range (1, x+1):
        answer *=n
    return answer

while True:
    try:
        w = int(input("Enter a number:"))# prompt user to input a value
        if w < 0: # checks if its positive or negative
            print("Please input a positive number!")
        else:
            break # breaks loop if positive number is entered
    except ValueError:
        print("Try again!")

print(f"Factorial:", factorial_use_loops(w))