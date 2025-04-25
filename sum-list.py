#cheking to add all real numbers entered
def sum_num():
    while True:
        try:
            # enter a list of real numbers
            values = input("Enter a list of numbers (separated by space):")
            values = values.split()

            # checking if all numbers entered are real numbers
            l = []
            for value in values:
                if float(value):
                    l.append(float(value))
            break
        except ValueError:
            print("All values should be real numbers!")

    total = sum(l)
    print("The sum is:", total)
sum_num()