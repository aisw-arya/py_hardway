
def loop():#Function create and append to a list and print it.
    range = 10
    increment = 2      
    i = 0
    numbers = []   #Empty list created.

    while i < range:    #To iterate until condition fail.
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

        print("The numbers: ")

        for num in numbers:
            print(num)


loop()      #function call


