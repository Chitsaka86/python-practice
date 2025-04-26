def reverse_string():
    s = ''
    data = input("Enter a string:")
    st = list(data)

    for inx in range(len(st)):
        s += st[-(inx + 1)]

    print("you reversed string is this:", s)


reverse_string()
