def even_or_odd():
    # ask user to input a number
    while True:
        try:
            m = input("Enter an integer number or 'done' to stop:")
            if m == "done":
                break
            m = int(m)

            # checking for odd and even number
            if m % 2 == 0:
                print(f"You put in an Even number!")
            else:
                print(f"You put in an Odd number!")
        except:
            print("This is not a number or done command")

even_or_odd()