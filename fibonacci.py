# simple program to print the fibonacci sequence to the desired number

while (True):
    count = input("Please enter a positive number and I will print the fibonacci sequence to that number (or type end): ")

    if (count.isnumeric() and int(count) > 0):
        # print fib seq
        numbers = [0,1,0]
        # print(str(numbers[2]) + "  " + str(numbers[1]) + "  ",end="")
        # need to handle edge case
        print(str(numbers[2]) + "  ",end="")
        if int(count) > 1:
            print(str(numbers[1]) + "  ",end="")
        count = int(count) - 2
        for i in range(count):
            numbers[0] = numbers[1] + numbers[2]
            print(str(numbers[0]) + "  ",end="")
            numbers.pop(2)
            numbers.insert(0, 0)

        print("")
        print("Ta daa")
        # exit()
    elif(count.lower() == "end"):
        exit()
    else: 
        print("Please enter a valid input")
